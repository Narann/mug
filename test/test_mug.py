import os
import tempfile
import unittest
from typing import Any

import mug


class TestWriteRead(unittest.TestCase):

    def setUp(self):
        _, self.temp_file_name = tempfile.mkstemp(prefix="mug_")

    def tearDown(self):
        os.remove(self.temp_file_name)

    def test_write_read(self):
        e1 = mug.Entity("foo")

        e1_1 = mug.Entity("bar")
        e1.children.append(e1_1)

        e1_1_attr = mug.Attribute("toto", mug.AttributeType.U8, 1)
        e1_1.attributes.append(e1_1_attr)

        with open(self.temp_file_name, 'wb') as fd:
            mug.write(fd, e1)

        with open(self.temp_file_name, 'rb') as fd:
            e2 = mug.read(fd)

        self.assertEqual(e2.name, e1.name)
        self.assertEqual(len(e2.children), len(e1.children))

        e2_1 = e2.children[0]

        self.assertEqual(e2_1.name, e1_1.name)


class TestWriteReadAttr(unittest.TestCase):

    def setUp(self):

        _, self.temp_file_name = tempfile.mkstemp(prefix="mug_")

    def _write_read_attr_common(self, type_: mug.AttributeType, value: Any):

        e1 = mug.Entity("foo")

        e1_attr = mug.Attribute("toto", type_, value)
        e1.attributes.append(e1_attr)

        with open(self.temp_file_name, 'wb') as fd:
            mug.write(fd, e1)

        with open(self.temp_file_name, 'rb') as fd:
            e2 = mug.read(fd)

        e2_attr = e2.attributes[0]

        self.assertEqual(e2_attr.name, e1_attr.name)
        self.assertEqual(e2_attr.type_, e1_attr.type_)

        return e1_attr.value, e2_attr.value

    def _write_read_attr(self, type_: mug.AttributeType, value: Any):

        e1_value, e2_value = self._write_read_attr_common(type_, value)

        self.assertEqual(e2_value, e1_value)

    def _write_read_attr_almost(self, type_: mug.AttributeType, value: Any,
                                places: int):

        e1_value, e2_value = self._write_read_attr_common(type_, value)

        self.assertAlmostEqual(e2_value, e1_value, places)

    def _write_read_attr_n(self, type_: mug.AttributeType, value: Any):

        e1_value, e2_value = self._write_read_attr_common(type_, value)

        self.assertIsInstance(e2_value, tuple)
        self.assertEqual(len(e1_value), len(e2_value))

        for e1_v, e2_v in zip(e1_value, e2_value):
            self.assertEqual(e2_v, e1_v)

    def _write_read_attr_n_almost(self, type_: mug.AttributeType, value: Any,
                                  places: int):

        e1_value, e2_value = self._write_read_attr_common(type_, value)

        self.assertIsInstance(e2_value, tuple)
        self.assertEqual(len(e1_value), len(e2_value))

        for e1_v, e2_v in zip(e1_value, e2_value):
            self.assertAlmostEqual(e2_v, e1_v, places)

    def test_attr_u8(self):
        self._write_read_attr(mug.AttributeType.U8, 42)

    def test_attr_u16(self):
        self._write_read_attr(mug.AttributeType.U16, 42)

    def test_attr_u32(self):
        self._write_read_attr(mug.AttributeType.U32, 42)

    def test_attr_u64(self):
        self._write_read_attr(mug.AttributeType.U64, 42)

    def test_attr_i8(self):
        self._write_read_attr(mug.AttributeType.I8, 42)

    def test_attr_i16(self):
        self._write_read_attr(mug.AttributeType.I16, 42)

    def test_attr_i32(self):
        self._write_read_attr(mug.AttributeType.I32, 42)

    def test_attr_i64(self):
        self._write_read_attr(mug.AttributeType.I64, 42)

    def test_attr_f16(self):
        self._write_read_attr_almost(mug.AttributeType.F16, 42.42, 1)

    def test_attr_f32(self):
        self._write_read_attr_almost(mug.AttributeType.F32, 42.42, 5)

    def test_attr_f64(self):
        self._write_read_attr(mug.AttributeType.F64, 42.42)

    def test_attr_str(self):
        self._write_read_attr(mug.AttributeType.STR, "tata")

    def test_attr_2u8(self):
        self._write_read_attr_n(mug.AttributeType.U8X2, (42, 43))

    def test_attr_2u16(self):
        self._write_read_attr_n(mug.AttributeType.U16X2, (42, 43))

    def test_attr_2u32(self):
        self._write_read_attr_n(mug.AttributeType.U32X2, (42, 43))

    def test_attr_2u64(self):
        self._write_read_attr_n(mug.AttributeType.U64X2, (42, 43))

    def test_attr_2i8(self):
        self._write_read_attr_n(mug.AttributeType.I8X2, (42, 43))

    def test_attr_2i16(self):
        self._write_read_attr_n(mug.AttributeType.I16X2, (42, 43))

    def test_attr_2i32(self):
        self._write_read_attr_n(mug.AttributeType.I32X2, (42, 43))

    def test_attr_2i64(self):
        self._write_read_attr_n(mug.AttributeType.I64X2, (42, 43))

    def test_attr_2f16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16X2, (42.42, 43.43),
                                       1)

    def test_attr_2f32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32X2, (42.42, 43.43),
                                       5)

    def test_attr_2f64(self):
        self._write_read_attr_n(mug.AttributeType.F64X2, (42.42, 43.43))

    def test_attr_3u8(self):
        self._write_read_attr_n(mug.AttributeType.U8X3, (42, 43, 44))

    def test_attr_3u16(self):
        self._write_read_attr_n(mug.AttributeType.U16X3, (42, 43, 44))

    def test_attr_3u32(self):
        self._write_read_attr_n(mug.AttributeType.U32X3, (42, 43, 44))

    def test_attr_3u64(self):
        self._write_read_attr_n(mug.AttributeType.U64X3, (42, 43, 44))

    def test_attr_3i8(self):
        self._write_read_attr_n(mug.AttributeType.I8X3, (42, 43, 44))

    def test_attr_3i16(self):
        self._write_read_attr_n(mug.AttributeType.I16X3, (42, 43, 44))

    def test_attr_3i32(self):
        self._write_read_attr_n(mug.AttributeType.I32X3, (42, 43, 44))

    def test_attr_3i64(self):
        self._write_read_attr_n(mug.AttributeType.I64X3, (42, 43, 44))

    def test_attr_3f16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16X3,
                                       (42.42, 43.43, 44.44),
                                       1)

    def test_attr_3f32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32X3,
                                       (42.42, 43.43, 44.44),
                                       5)

    def test_attr_3f64(self):
        self._write_read_attr_n(mug.AttributeType.F64X3, (42.42, 43.43, 44.44))

    def test_attr_4u8(self):
        self._write_read_attr_n(mug.AttributeType.U8X4, (42, 43, 44, 45))

    def test_attr_4u16(self):
        self._write_read_attr_n(mug.AttributeType.U16X4, (42, 43, 44, 45))

    def test_attr_4u32(self):
        self._write_read_attr_n(mug.AttributeType.U32X4, (42, 43, 44, 45))

    def test_attr_4u64(self):
        self._write_read_attr_n(mug.AttributeType.U64X4, (42, 43, 44, 45))

    def test_attr_4i8(self):
        self._write_read_attr_n(mug.AttributeType.I8X4, (42, 43, 44, 45))

    def test_attr_4i16(self):
        self._write_read_attr_n(mug.AttributeType.I16X4, (42, 43, 44, 45))

    def test_attr_4i32(self):
        self._write_read_attr_n(mug.AttributeType.I32X4, (42, 43, 44, 45))

    def test_attr_4i64(self):
        self._write_read_attr_n(mug.AttributeType.I64X4, (42, 43, 44, 45))

    def test_attr_4f16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16X4, (42.42, 43.43,
                                                                 44.44, 45.45),
                                       1)

    def test_attr_4f32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32X4, (42.42, 43.43,
                                                                 44.44, 45.45),
                                       5)

    def test_attr_4f64(self):
        self._write_read_attr_n(mug.AttributeType.F64X4, (42.42, 43.43, 44.44,
                                                          45.45))

    def test_attr_9u8(self):
        self._write_read_attr_n(mug.AttributeType.U8X9, (42, 43, 44, 45, 46,
                                                         47, 48, 49, 50))

    def test_attr_9u16(self):
        self._write_read_attr_n(mug.AttributeType.U16X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9u32(self):
        self._write_read_attr_n(mug.AttributeType.U32X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9u64(self):
        self._write_read_attr_n(mug.AttributeType.U64X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9i8(self):
        self._write_read_attr_n(mug.AttributeType.I8X9, (42, 43, 44, 45, 46,
                                                         47, 48, 49, 50))

    def test_attr_9i16(self):
        self._write_read_attr_n(mug.AttributeType.I16X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9i32(self):
        self._write_read_attr_n(mug.AttributeType.I32X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9i64(self):
        self._write_read_attr_n(mug.AttributeType.I64X9, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50))

    def test_attr_9f16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16X9, (42.42, 43.43,
                                                                 44.44, 45.45,
                                                                 46.46, 47.47,
                                                                 48.48, 49.49,
                                                                 50.50), 1)

    def test_attr_9f32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32X9, (42.42, 43.43,
                                                                 44.44, 45.45,
                                                                 46.46, 47.47,
                                                                 48.48, 49.49,
                                                                 50.50), 5)

    def test_attr_9f64(self):
        self._write_read_attr_n(mug.AttributeType.F64X9, (42.42, 43.43, 44.44,
                                                          45.45, 46.46, 47.47,
                                                          48.48, 49.49, 50.50))

    def test_attr_16u8(self):
        self._write_read_attr_n(mug.AttributeType.U8X16, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50, 51,
                                                          52, 53, 54, 55, 56,
                                                          57))

    def test_attr_16u16(self):
        self._write_read_attr_n(mug.AttributeType.U16X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16u32(self):
        self._write_read_attr_n(mug.AttributeType.U32X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16u64(self):
        self._write_read_attr_n(mug.AttributeType.U64X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16i8(self):
        self._write_read_attr_n(mug.AttributeType.I8X16, (42, 43, 44, 45, 46,
                                                          47, 48, 49, 50, 51,
                                                          52, 53, 54, 55, 56,
                                                          57))

    def test_attr_16i16(self):
        self._write_read_attr_n(mug.AttributeType.I16X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16i32(self):
        self._write_read_attr_n(mug.AttributeType.I32X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16i64(self):
        self._write_read_attr_n(mug.AttributeType.I64X16, (42, 43, 44, 45, 46,
                                                           47, 48, 49, 50, 51,
                                                           52, 53, 54, 55, 56,
                                                           57))

    def test_attr_16f16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16X16, (42.42, 43.43,
                                                                  44.44, 45.45,
                                                                  46.46, 47.47,
                                                                  48.48, 49.49,
                                                                  50.50, 51.51,
                                                                  52.52, 53.53,
                                                                  54.54, 55.55,
                                                                  56.56, 57.57),
                                       1)

    def test_attr_16f32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32X16, (42.42, 43.43,
                                                                  44.44, 45.45,
                                                                  46.46, 47.47,
                                                                  48.48, 49.49,
                                                                  50.50, 51.51,
                                                                  52.52, 53.53,
                                                                  54.54, 55.55,
                                                                  56.56, 57.57),
                                       5)

    def test_attr_16f64(self):
        self._write_read_attr_n(mug.AttributeType.F64X16, (42.42, 43.43, 44.44,
                                                           45.45, 46.46, 47.47,
                                                           48.48, 49.49, 50.50,
                                                           51.51, 52.52, 53.53,
                                                           54.54, 55.55, 56.56,
                                                           57.57), )

    def test_attr_nu8(self):
        self._write_read_attr_n(mug.AttributeType.U8_ARRAY, (42, 43, 44, 45, 46,
                                                             47, 48, 49, 50, 51,
                                                             52, 53, 54, 55, 56,
                                                             57))

    def test_attr_nu16(self):
        self._write_read_attr_n(mug.AttributeType.U16_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_nu32(self):
        self._write_read_attr_n(mug.AttributeType.U32_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_nu64(self):
        self._write_read_attr_n(mug.AttributeType.U64_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_ni8(self):
        self._write_read_attr_n(mug.AttributeType.I8_ARRAY, (42, 43, 44, 45,
                                                             46, 47, 48, 49,
                                                             50, 51, 52, 53,
                                                             54, 55, 56, 57))

    def test_attr_ni16(self):
        self._write_read_attr_n(mug.AttributeType.I16_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_ni32(self):
        self._write_read_attr_n(mug.AttributeType.I32_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_ni64(self):
        self._write_read_attr_n(mug.AttributeType.I64_ARRAY, (42, 43, 44, 45,
                                                              46, 47, 48, 49,
                                                              50, 51, 52, 53,
                                                              54, 55, 56, 57))

    def test_attr_nf16(self):
        self._write_read_attr_n_almost(mug.AttributeType.F16_ARRAY, (42.42,
                                                                     43.43,
                                                                     44.44,
                                                                     45.45,
                                                                     46.46,
                                                                     47.47,
                                                                     48.48,
                                                                     49.49,
                                                                     50.50,
                                                                     51.51,
                                                                     52.52,
                                                                     53.53,
                                                                     54.54,
                                                                     55.55,
                                                                     56.56), 1)

    def test_attr_nf32(self):
        self._write_read_attr_n_almost(mug.AttributeType.F32_ARRAY,
                                       (42.42, 43.43, 44.44, 45.45,
                                        46.46, 47.47, 48.48, 49.49,
                                        50.50, 51.51, 52.52, 53.53,
                                        54.54, 55.55, 56.56), 5)

    def test_attr_nf64(self):
        self._write_read_attr_n(mug.AttributeType.F64_ARRAY,
                                (42.42, 43.43, 44.44, 45.45, 46.46,
                                 47.47, 48.48, 49.49, 50.50, 51.51,
                                 52.52, 53.53, 54.54, 55.55, 56.56))
