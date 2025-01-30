#include "py/runtime.h"

STATIC mp_obj_t fast_shade(mp_obj_t normal_x, mp_obj_t normal_y, 
                           mp_obj_t light_x, mp_obj_t light_y) {
    float nx = mp_obj_get_float(normal_x);
    float ny = mp_obj_get_float(normal_y);
    float lx = mp_obj_get_float(light_x);
    float ly = mp_obj_get_float(light_y);

    float intensity = fmax(0, nx * lx + ny * ly);
    return mp_obj_new_int((int)(255 * intensity));
}
STATIC MP_DEFINE_CONST_FUN_OBJ_4(fast_shade_obj, fast_shade);

STATIC const mp_rom_map_elem_t fast_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR_fast_shade), MP_ROM_PTR(&fast_shade_obj) },
};
STATIC MP_DEFINE_CONST_DICT(fast_module_globals, fast_module_globals_table);

const mp_obj_module_t fast_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&fast_module_globals,
};

MP_REGISTER_MODULE(MP_QSTR_fast, fast_module);
