#!/usr/bin/env python3

import os
import shutil
import glob  # в начале файла, если ещё не подключён

DATA_SECTION_START_ADDRESS = 184
DEBUG = False

# ваш список patches остаётся без изменений
#from patches import patches  # предполагается, что список вынесен в отдельный файл (см. ниже), иначе вставьте весь код сюда


patches = [
    {
        'patch_name': 'Advanced Noise Reduction ALL (luma+chroma)',
        'module_name': 'anr10_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'ANR10 - ONLY Luma Noise Reduction - TEST IT',
        'module_name': 'anr10_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 76,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'ANR10 - ONLY Chroma Noise Reduction - TEST IT',
        'module_name': 'anr10_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 80,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Hybrid Noise Reduction',
        'module_name': 'hnr10_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Low Exposure? Noise Reduction',
        'module_name': 'lenr10_ipe',  # module name
        'address_offset': 34,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Adaptive Spatial Filter ALL (Sharpening)',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Adaptive Spatial Filter - ONLY Edge Detection (layer 1) - TEST IT',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 108,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Adaptive Spatial Filter - ONLY Edge Detection (layer 2) - TEST IT',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 112,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Adaptive Spatial Filter - ONLY Edge Detection (radial) - TEST IT',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 116,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Adaptive Spatial Filter - ONLY Edge Detection (contrast) - TEST IT',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 120,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Tone Mapping Control v10',
        'module_name': 'tmc10_sw',  # module name
        'address_offset': 36,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Tone Mapping Control v11',
        'module_name': 'tmc11_sw',  # module name
        'address_offset': 36,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Tone Mapping Control v12',
        'module_name': 'tmc12_sw',  # module name
        'address_offset': 36,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Tone Mapping Control v13',
        'module_name': 'tmc13_sw',  # module name
        'address_offset': 36,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Global Tone Mapping (RAW)',
        'module_name': 'gtm10_ife',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Global Tone Mapping (YUV 4:2:0)',
        'module_name': 'gtm13_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Local Tone Mapping v13',
        'module_name': 'ltm13_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Local Tone Mapping v14',
        'module_name': 'ltm14_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Local Tone Mapping v15',
        'module_name': 'ltm15_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x' find
        'replace': '00',  # hex without '0x' replace
    },
    {
        'patch_name': 'Local Tone Mapping v16',
        'module_name': 'ltm16_ipe',  # module name
        'address_offset': 35,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'RAW Gamma curve (65 dots) (Video signal, JPG Preview) (!!!for testing only!!!)',
        'module_name': 'gamma16_ife',  # module name
        'address_offset': 33,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'YUV 4:2:0 - Gamma curve (257 dots) (Video Signal, JPG Signal) (!!!for testing only!!!)',
        'module_name': 'gamma16_ipe',  # module name
        'address_offset': 33,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'RAW Gamma curve (65 dots) (JPG Signal) (!!!for testing only!!!)',
        'module_name': 'gamma16_bps',  # module name
        'address_offset': 33,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Multi Frame - does not cause ghosting. Used for sharpening?',
        'module_name': 'mf10_sw',  # module name
        'address_offset': 37,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Multi Frame - does not cause ghosting. Used for sharpening?',
        'module_name': 'mf11_sw',  # module name
        'address_offset': 37,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Temporal Filter v10 (aka MFNR - Multi Frame Noise Reduction) - causes ghosting. !!! you must disable ANR entirely when using this !!!',
        'module_name': 'tf10_ipe',  # module name
        'address_offset': 36,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'Temporal Filter v20 (aka MFNR - Multi Frame Noise Reduction) - causes ghosting. !!! you must disable ANR entirely when using this !!!',
        'module_name': 'tf20_ipe',  # module name
        'address_offset': 36,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },

] 


def hex_to_big_little_int(hex_str):
    little_hex = bytearray.fromhex(hex_str)
    little_hex.reverse()
    return int(little_hex.hex(), 16)


def patch_process(filepath, patch_indices):
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())

    datasectionoffset = hex_to_big_little_int(data[DATA_SECTION_START_ADDRESS:DATA_SECTION_START_ADDRESS + 4].hex())
    if DEBUG:
        print(f"data section offset int32: {datasectionoffset}\n")

    for n in patch_indices:
        patch = patches[n]
        module_bytes = patch['module_name'].encode('utf-8')
        search_bytes = bytes.fromhex(patch['search'])
        replace_bytes = bytes.fromhex(patch['replace'])

        start = 0
        found_count = 0
        matches = 0

        print(f"\n[{patch['module_name']}] searching...")

        while True:
            idx = data.find(module_bytes, start)
            if idx == -1:
                break

            found_count += 1
            address_ptr = idx + len(module_bytes) + patch['address_offset']
            if address_ptr + 4 > len(data):
                break

            offset_bytes = data[address_ptr:address_ptr + 4]
            offset = hex_to_big_little_int(offset_bytes.hex())
            patch_location = datasectionoffset + offset + patch['data_offset']

            if patch_location + len(search_bytes) > len(data):
                break

            current_value = data[patch_location:patch_location + len(search_bytes)]

            if current_value == search_bytes:
                print(f"\t#{found_count:>3}. patching {current_value.hex()} -> {patch['replace']}")
                data[patch_location:patch_location + len(replace_bytes)] = replace_bytes
                matches += 1
            else:
                print(f"\t#{found_count:>3}. already {current_value.hex()}")

            start = idx + 1

        print(f"Patched {matches} of {found_count} occurrences.")

    with open(filepath, 'wb') as f:
        f.write(data)




def patch_start():
    filename = input(
        '\nEnter the full file name of your tuning .bin\nLeave empty to patch all .bin files in /input\n------\n: ').strip()

    if filename == "":
        file_list = sorted(glob.glob('input/*.bin'))
        if not file_list:
            print("No .bin files found in /input. Aborting.")
            return
        print(f"\n{len(file_list)} file(s) found:")
        for name in file_list:
            print(" -", os.path.basename(name))
    else:
        input_path = os.path.join('input', filename)
        if not os.path.exists(input_path):
            print("Selected file doesn't exist. Aborting..")
            return
        file_list = [input_path]

    print('\nFollowing patches are available:\n')
    for i, patch in enumerate(patches):
        print(f"{i:>2}. {patch['module_name']:<12} [{patch['patch_name']}]")

    str_arr = input('\nEnter your desired patch(es) separated by comma (e.g., 0,1,5,7), or [all]: ').strip()
    if str_arr.lower() == 'all':
        patch_arr = list(range(len(patches)))
    else:
        patch_arr = list(map(int, str_arr.split(',')))

    for inputFile in file_list:
        outputFile = os.path.join('output', os.path.basename(inputFile))
        if os.path.exists(outputFile):
            os.remove(outputFile)
        shutil.copyfile(inputFile, outputFile)

        print(f"\nProcessing: {os.path.basename(inputFile)}")
        patch_process(outputFile, patch_arr)

    print("\nAll patches have been applied!\n\nPress Enter to exit ...")
    input()


def main():
    patch_start()


if __name__ == '__main__':
    main()
