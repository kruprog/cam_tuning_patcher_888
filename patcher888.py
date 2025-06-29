#/usr/bin/env python3

import os
import shutil

DATA_SECTION_START_ADDRESS = 0xB8
DEBUG = False

patches = [
    {
        'patch_name': 'Advanced Noise Reduction Module (luma+chroma)',
        'module_name': 'anr10_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    # {
    #     'patch_name': 'ANR10 - Disable Chroma Noise Reduction',
    #     'module_name': 'anr10_ipe',  # module name
    #     'address_offset': 35,   # bytes from module name to data section address
    #     'data_offset': ,  # bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
    # {
    #     'patch_name': 'ANR10 - Disable Luma Noise Reduction',
    #     'module_name': 'anr10_ipe',  # module name
    #     'address_offset': 35,   # bytes from module name to data section address
    #     'data_offset': 152,  # bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
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
        'patch_name': 'Adaptive Spatial Filter Module (Sharpening)',
        'module_name': 'asf30_ipe',  # module name
        'address_offset': 35,   # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    # {
    #     'patch_name': 'ASF30 - Disable Edge Detection (layer 1)',
    #     'module_name': 'asf30_ipe',  # module name
    #     'address_offset': 35,  # bytes from module name to data section address
    #     'data_offset': 200,  bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
    # {
    #     'patch_name': 'ASF30 - Disable Edge Detection (layer 2)',
    #     'module_name': 'asf30_ipe',  # module name
    #     'address_offset': 35,  # bytes from module name to data section address
    #     'data_offset': 208,  bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
    # {
    #     'patch_name': 'ASF30 - Disable Edge Detection (radial)',
    #     'module_name': 'asf30_ipe',  # module name
    #     'address_offset': 35,  # bytes from module name to data section address
    #     'data_offset': 216,  bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
    # {
    #     'patch_name': 'ASF30 - Disable Edge Detection (contrast)',
    #     'module_name': 'asf30_ipe',  # module name
    #     'address_offset': 35,  # bytes from module name to data section address
    #     'data_offset': 224,  bytes from beginning of module data section
    #     'search': '01',  # hex without '0x'
    #     'replace': '00',  # hex without '0x'
    # },
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
        'patch_name': 'RAW Gamma curve (65 dots) (Video signal, JPG Preview)',
        'module_name': 'gamma16_ife',  # module name
        'address_offset': 33,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'YUV 4:2:0 - Gamma curve (257 dots) (Video Signal, JPG Signal)',
        'module_name': 'gamma16_ipe',  # module name
        'address_offset': 33,  # bytes from module name to data section address
        'data_offset': 0,  # bytes from beginning of module data section
        'search': '01',  # hex without '0x'
        'replace': '00',  # hex without '0x'
    },
    {
        'patch_name': 'RAW Gamma curve (65 dots) (JPG Signal)',
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


def patch_start(patches=None):
    filename = input(
        '\nEnter the full file name of your tuning .bin\nExample: com.qti.tuned.umi_semco_s5khmx.bin\n------\n: ')

    inputFile = 'input/' + filename
    outputFile = 'output/' + filename

    patchNum = 0

    if not os.path.exists(inputFile):
        print("Selected file doesn't exist. Aborting..")
        return

    #create output file
    if os.path.exists(outputFile):
        os.remove(outputFile)
    shutil.copyfile(inputFile, outputFile)

    #list all patches
    print('\nFollowing patches are available:\n')
    for patch in patches:
        print(f"{str(patchNum):>2}. {patch['module_name']:<12} [{patch['patch_name']}]")
        patchNum = patchNum + 1

    #patch selection input
    str_arr = input('\nEnter your desired patch(es). Separated by comma [,] (example: 0,1,5,7) or to apply every patch type [all] (example: all) : ')

    #convert string input to integer list
    if str_arr != 'all':
        str_arr = str_arr.split(',')
        patch_arr = list(map(int, str_arr))
    else:
        i = 0
        patch_arr = []
        for patch in patches:
            patch_arr.append(i)
            i = i + 1

    #execute patching process for each selected patch
    for n in patch_arr:
        patch_process(outputFile, n)

    #avoid exit without user input
    print("\nAll patches have been applied!\n\nPress Enter to exit ...")
    #input()


#convert hex x86 to arm. or other way around idk
def hex_to_big_little_int(hex):
    little_hex = bytearray.fromhex(hex)
    little_hex.reverse()
    str_little = ''.join(format(x, '02x') for x in little_hex)
    int_little = int(str_little, base=16)
    return int_little


def patch_process(outputFile, n):
    with open(outputFile, 'r+b') as f:
        for index, patch in enumerate(patches):
            #checks if current list index is selected to be patched by user
            if index == n:
                f.seek(0)
                data = f.read()
                #counts all string search hits
                num_hit = data.count(str.encode(patch['module_name']))
                print('\n' + '[' + patch['module_name'] + ']' + ' has been found ' + str(num_hit) + ' times: ')
                count = 0
                matches = 0
                # goes to offset which contains data section address
                f.seek(DATA_SECTION_START_ADDRESS)

                # read the data section offset
                datasectionoffset = hex_to_big_little_int(f.read(4).hex())



                print('data section offset int32: ' + str(datasectionoffset) + '\n') if DEBUG else None

                #goes back to file beginning
                f.seek(0)

                i = 1

                #repeats until break
                while True:
                    #save current location for later use
                    location = f.tell()
                    string = patch['module_name'].encode('utf-8')
                    #checks for current patching hit. avoids infinite while True: loop from never stopping
                    if f.read(len(string)).hex() == string.hex() and count < num_hit:
                        print('found data for ' + patch['module_name']) if DEBUG else None
                        #save current location for later use
                        location = f.tell()
                        #go from patch['module_name'] to offset that stores the data block offset
                        f.seek(location + patch['address_offset'])
                        #read the module_name data block offset
                        offset = f.read(4).hex()
                        #convert offset hex to int
                        offset_little_int = hex_to_big_little_int(offset)
                        print('offset hex: ' + offset) if DEBUG else None
                        print('offset int32: ' + str(offset_little_int)) if DEBUG else None
                        #go to module_name data block and go to offset that has to be patched
                        f.seek(offset_little_int + datasectionoffset)
                        print(patch['module_name'] + ' block offset int32: ' + str(f.tell())) if DEBUG else None
                        f.read(patch['data_offset'])
                        #save offset for later use
                        new_offset = f.tell()
                        print('value offset from file beginning int32: ' + str(new_offset)) if DEBUG else None
                        #go back to previous location
                        f.seek(new_offset)
                        #checks if original byte == patch['search'] byte
                        data_value = f.read(len(patch['search']) // 2).hex()

                        print(f'>{data_value}< == >{patch["search"]}<') if DEBUG else None

                        if data_value == patch['search']:
                            print(f'\t#{i:>3}. changing: {data_value}', end='')
                            #go back to previous location
                            f.seek(new_offset)
                            #patch byte(s)
                            f.write(bytes.fromhex(patch['replace']))
                            #go back to previous location
                            f.seek(new_offset)
                            print(' --> ' + str(f.read(len(patch['replace']) // 2).hex()))
                            matches += 1
                        else:
                            print(f'\t#{i:>3}.  already: {data_value}')

                        i += 1
                        #goes back to origin location
                        f.seek(location)
                        count += 1
                    elif count < num_hit:
                        #goes one byte or whatever further than the last hit, to prevent patching the same hit infinite times
                        f.seek(location + 1)
                    #checks if all hits have been patched
                    elif count >= num_hit:
                        #close the patched file
                        f.close()
                        break


def main():
    patch_start(patches=patches)


if __name__ == '__main__':
    main()
