# How to Use the Patcher

### Steps:

1. **Place your tuning bin** into the `input` folder.  
2. **Run the patcher** by opening `run888.bat`.  
3. **Follow the instructions** in the command line.  
4. After patching, the files will be located in the `output` folder.

> ⚠️ **Note:** Do **not** disable the **Gamma** module — it is included for testing purposes only.

Effects:
0,1,2,3,4 - noise reduction full disable, MFNR enabled.
1,3,4 - Only color noise reduction works. MFNR enabled.
26 - MFNR disabled. No ghosting anymore.
17 - local tone mapping disabled. No flickering in video with manual exposure settings. Affects contrast, lower contrast in shadow regions.
22 - affects contrast. Makes image darker and more contrast.
15, 19 - doesn't recommended to use. Crashes HDR video mode in stock camera.
5,6,7,8,9 - disables sharpening.
10,11,18  - not used in libraries mi 11 ultra. No effect.
12,13,14,16,20,23,24,25 - effect unknown. No visible effect in my tests.

Practically useful combinations:

0,1,2,3,4,17,26
1,3,4,17,26
0,1,2,3,4,12,13,14,16,17,23,24,25,26
1,3,4,12,13,14,16,17,23,24,25,26
