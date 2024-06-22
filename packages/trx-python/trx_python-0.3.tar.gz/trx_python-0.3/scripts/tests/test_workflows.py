#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from deepdiff import DeepDiff
import os
import tempfile

import pytest
import numpy as np
from numpy.testing import assert_equal, assert_array_equal, assert_allclose
try:
    from dipy.io.streamline import load_tractogram
    dipy_available = True
except ImportError:
    dipy_available = False

from trx.fetcher import (get_testing_files_dict,
                         fetch_data, get_home)
import trx.trx_file_memmap as tmm
from trx.workflows import (convert_dsi_studio,
                           convert_tractogram,
                           manipulate_trx_datatype,
                           generate_trx_from_scratch,
                           validate_tractogram,)


# If they already exist, this only takes 5 seconds (check md5sum)
fetch_data(get_testing_files_dict(), keys=['DSI.zip', 'trx_from_scratch.zip'])


def test_help_option_convert_dsi(script_runner):
    ret = script_runner.run('tff_convert_dsi_studio.py', '--help')
    assert ret.success


def test_help_option_convert(script_runner):
    ret = script_runner.run('tff_convert_tractogram.py', '--help')
    assert ret.success


def test_help_option_generate_trx_from_scratch(script_runner):
    ret = script_runner.run('tff_generate_trx_from_scratch.py', '--help')
    assert ret.success


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_convert_dsi():
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_trk = os.path.join(get_home(), 'DSI',
                              'CC.trk.gz')
        in_nii = os.path.join(get_home(), 'DSI',
                              'CC.nii.gz')
        exp_data = os.path.join(get_home(), 'DSI',
                                'CC_fix_data.npy')
        exp_offsets = os.path.join(get_home(), 'DSI',
                                   'CC_fix_offsets.npy')
        out_fix_path = os.path.join(tmp_dir, 'fixed.trk')
        convert_dsi_studio(in_trk, in_nii, out_fix_path,
                           remove_invalid=False,
                           keep_invalid=True)

        data_fix = np.load(exp_data)
        offsets_fix = np.load(exp_offsets)

        sft = load_tractogram(out_fix_path, 'same')
        assert_equal(sft.streamlines._data, data_fix)
        assert_equal(sft.streamlines._offsets, offsets_fix)


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_convert_to_trx():
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_trk = os.path.join(get_home(), 'DSI',
                              'CC_fix.trk')
        exp_data = os.path.join(get_home(), 'DSI',
                                'CC_fix_data.npy')
        exp_offsets = os.path.join(get_home(), 'DSI',
                                   'CC_fix_offsets.npy')
        out_trx_path = os.path.join(tmp_dir, 'CC_fix.trx')
        convert_tractogram(in_trk, out_trx_path, None)

        data_fix = np.load(exp_data)
        offsets_fix = np.load(exp_offsets)

        trx = tmm.load(out_trx_path)
        assert_equal(trx.streamlines._data.dtype, np.float32)
        assert_equal(trx.streamlines._offsets.dtype, np.uint32)
        assert_array_equal(trx.streamlines._data, data_fix)
        assert_array_equal(trx.streamlines._offsets, offsets_fix)
        trx.close()


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_convert_from_trx():
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_trk = os.path.join(get_home(), 'DSI',
                              'CC_fix.trk')
        in_nii = os.path.join(get_home(), 'DSI',
                              'CC.nii.gz')
        exp_data = os.path.join(get_home(), 'DSI',
                                'CC_fix_data.npy')
        exp_offsets = os.path.join(get_home(), 'DSI',
                                   'CC_fix_offsets.npy')

        # Sequential conversions
        out_trx_path = os.path.join(tmp_dir, 'CC_fix.trx')
        out_trk_path = os.path.join(tmp_dir, 'CC_fix.trk')
        out_tck_path = os.path.join(tmp_dir, 'CC_fix.tck')
        convert_tractogram(in_trk, out_trx_path, None)
        convert_tractogram(out_trx_path, out_tck_path, None)
        convert_tractogram(out_trx_path, out_trk_path, None)

        data_fix = np.load(exp_data)
        offsets_fix = np.load(exp_offsets)

        sft = load_tractogram(out_trk_path, 'same')
        assert_equal(sft.streamlines._data, data_fix)
        assert_equal(sft.streamlines._offsets, offsets_fix)

        sft = load_tractogram(out_tck_path, in_nii)
        assert_equal(sft.streamlines._data, data_fix)
        assert_equal(sft.streamlines._offsets, offsets_fix)


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_convert_dtype_p16_o64():
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_trk = os.path.join(get_home(), 'DSI',
                              'CC_fix.trk')
        out_convert_path = os.path.join(tmp_dir, 'CC_fix_p16_o64.trx')
        convert_tractogram(in_trk, out_convert_path, None,
                           pos_dtype='float16', offsets_dtype='uint64')

        trx = tmm.load(out_convert_path)
        assert_equal(trx.streamlines._data.dtype, np.float16)
        assert_equal(trx.streamlines._offsets.dtype, np.uint64)
        trx.close()


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_convert_dtype_p64_o32():
    with tempfile.TemporaryDirectory() as tmp_dir:
        in_trk = os.path.join(get_home(), 'DSI',
                              'CC_fix.trk')
        out_convert_path = os.path.join(tmp_dir, 'CC_fix_p16_o64.trx')
        convert_tractogram(in_trk, out_convert_path, None,
                           pos_dtype='float64', offsets_dtype='uint32')

        trx = tmm.load(out_convert_path)
        assert_equal(trx.streamlines._data.dtype, np.float64)
        assert_equal(trx.streamlines._offsets.dtype, np.uint32)
        trx.close()


def test_execution_generate_trx_from_scratch():
    with tempfile.TemporaryDirectory() as tmp_dir:
        reference_fa = os.path.join(get_home(), 'trx_from_scratch',
                                    'fa.nii.gz')
        raw_arr_dir = os.path.join(get_home(), 'trx_from_scratch',
                                   'test_npy')
        expected_trx = os.path.join(get_home(), 'trx_from_scratch',
                                    'expected.trx')

        dpv = [(os.path.join(raw_arr_dir, 'dpv_cx.npy'), 'uint8'),
               (os.path.join(raw_arr_dir, 'dpv_cy.npy'), 'uint8'),
               (os.path.join(raw_arr_dir, 'dpv_cz.npy'), 'uint8')]
        dps = [(os.path.join(raw_arr_dir, 'dps_algo.npy'), 'uint8'),
               (os.path.join(raw_arr_dir, 'dps_cw.npy'), 'float64')]
        dpg = [('g_AF_L', os.path.join(raw_arr_dir, 'dpg_AF_L_mean_fa.npy'), 'float32'),
               ('g_AF_R', os.path.join(raw_arr_dir, 'dpg_AF_R_mean_fa.npy'), 'float32'),
               ('g_AF_L', os.path.join(raw_arr_dir, 'dpg_AF_L_volume.npy'), 'float32')]
        groups = [(os.path.join(raw_arr_dir, 'g_AF_L.npy'), 'int32'),
                  (os.path.join(raw_arr_dir, 'g_AF_R.npy'), 'int32'),
                  (os.path.join(raw_arr_dir, 'g_CST_L.npy'), 'int32')]

        out_gen_path = os.path.join(tmp_dir, 'generated.trx')
        generate_trx_from_scratch(reference_fa, out_gen_path,
                                  positions=os.path.join(raw_arr_dir,
                                                         'positions.npy'),
                                  offsets=os.path.join(raw_arr_dir,
                                                       'offsets.npy'),
                                  positions_dtype='float16',
                                  offsets_dtype='uint64',
                                  space_str='rasmm', origin_str='nifti',
                                  verify_invalid=False, dpv=dpv, dps=dps,
                                  groups=groups, dpg=dpg)
        exp_trx = tmm.load(expected_trx)
        gen_trx = tmm.load(out_gen_path)

        assert DeepDiff(exp_trx.get_dtype_dict(),
                        gen_trx.get_dtype_dict()) == {}

        assert_allclose(exp_trx.streamlines._data, gen_trx.streamlines._data,
                        atol=0.1, rtol=0.1)
        assert_equal(exp_trx.streamlines._offsets,
                     gen_trx.streamlines._offsets)

        for key in exp_trx.data_per_vertex.keys():
            assert_equal(exp_trx.data_per_vertex[key]._data,
                         gen_trx.data_per_vertex[key]._data)
            assert_equal(exp_trx.data_per_vertex[key]._offsets,
                         gen_trx.data_per_vertex[key]._offsets)
        for key in exp_trx.data_per_streamline.keys():
            assert_equal(exp_trx.data_per_streamline[key],
                         gen_trx.data_per_streamline[key])
        for key in exp_trx.groups.keys():
            assert_equal(exp_trx.groups[key], gen_trx.groups[key])

        for group in exp_trx.groups.keys():
            if group in exp_trx.data_per_group:
                for key in exp_trx.data_per_group[group].keys():
                    assert_equal(exp_trx.data_per_group[group][key],
                                 gen_trx.data_per_group[group][key])
        exp_trx.close()
        gen_trx.close()


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_concatenate_validate_trx():
    with tempfile.TemporaryDirectory() as tmp_dir:
        trx1 = tmm.load(os.path.join(get_home(), 'gold_standard',
                                     'gs.trx'))
        trx2 = tmm.load(os.path.join(get_home(), 'gold_standard',
                                     'gs.trx'))
        # trx2.streamlines._data += 0.001
        trx = tmm.concatenate([trx1, trx2], preallocation=False)

        # Right size
        assert_equal(len(trx.streamlines), 2*len(trx1.streamlines))

        # Right data
        end_idx = trx1.header['NB_VERTICES']
        assert_allclose(
            trx.streamlines._data[:end_idx], trx1.streamlines._data)
        assert_allclose(
            trx.streamlines._data[end_idx:], trx2.streamlines._data)

        # Right data_per_*
        for key in trx.data_per_vertex.keys():
            assert_equal(trx.data_per_vertex[key]._data[:end_idx],
                         trx1.data_per_vertex[key]._data)
            assert_equal(trx.data_per_vertex[key]._data[end_idx:],
                         trx2.data_per_vertex[key]._data)

        end_idx = trx1.header['NB_STREAMLINES']
        for key in trx.data_per_streamline.keys():
            assert_equal(trx.data_per_streamline[key][:end_idx],
                         trx1.data_per_streamline[key])
            assert_equal(trx.data_per_streamline[key][end_idx:],
                         trx2.data_per_streamline[key])

        # Validate
        out_concat_path = os.path.join(tmp_dir, 'concat.trx')
        out_valid_path = os.path.join(tmp_dir, 'valid.trx')
        tmm.save(trx, out_concat_path)
        validate_tractogram(out_concat_path, None, out_valid_path,
                            remove_identical_streamlines=True,
                            precision=0)
        trx_val = tmm.load(out_valid_path)

        # # Right dtype and size
        assert DeepDiff(trx.get_dtype_dict(), trx_val.get_dtype_dict()) == {}
        assert_equal(len(trx1.streamlines), len(trx_val.streamlines))

        trx.close()
        trx1.close()
        trx2.close()
        trx_val.close()


@pytest.mark.skipif(not dipy_available,
                    reason='Dipy is not installed.')
def test_execution_manipulate_trx_datatype():
    with tempfile.TemporaryDirectory() as tmp_dir:
        expected_trx = os.path.join(get_home(), 'trx_from_scratch',
                                    'expected.trx')
        trx = tmm.load(expected_trx)

        expected_dtype = {'positions': np.dtype('float16'),
                          'offsets': np.dtype('uint64'),
                          'dpv': {'dpv_cx': np.dtype('uint8'),
                                  'dpv_cy': np.dtype('uint8'),
                                  'dpv_cz': np.dtype('uint8')},
                          'dps': {'dps_algo': np.dtype('uint8'),
                                  'dps_cw': np.dtype('float64')},
                          'dpg': {'g_AF_L':
                                  {'dpg_AF_L_mean_fa': np.dtype('float32'),
                                   'dpg_AF_L_volume': np.dtype('float32')},
                                  'g_AF_R':
                                  {'dpg_AF_R_mean_fa': np.dtype('float32')}},
                          'groups': {'g_AF_L': np.dtype('int32'),
                                     'g_AF_R': np.dtype('int32')}}

        assert DeepDiff(trx.get_dtype_dict(), expected_dtype) == {}
        trx.close()

        generated_dtype = {'positions': np.dtype('float32'),
                           'offsets': np.dtype('uint32'),
                           'dpv': {'dpv_cx': np.dtype('uint16'),
                                   'dpv_cy': np.dtype('uint16'),
                                   'dpv_cz': np.dtype('uint16')},
                           'dps': {'dps_algo': np.dtype('uint8'),
                                   'dps_cw': np.dtype('float32')},
                           'dpg': {'g_AF_L':
                                   {'dpg_AF_L_mean_fa': np.dtype('float64'),
                                    'dpg_AF_L_volume': np.dtype('float32')},
                                   'g_AF_R':
                                   {'dpg_AF_R_mean_fa': np.dtype('float64')}},
                           'groups': {'g_AF_L': np.dtype('uint16'),
                                      'g_AF_R': np.dtype('uint16')}}

        out_gen_path = os.path.join(tmp_dir, 'generated.trx')
        manipulate_trx_datatype(expected_trx, out_gen_path, generated_dtype)
        trx = tmm.load(out_gen_path)
        assert DeepDiff(trx.get_dtype_dict(), generated_dtype) == {}
        trx.close()
