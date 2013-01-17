# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF arabic'
    native_name = u''

    def glyphs(self):
        # arabic subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = [0x000D, 0x0020, 0x0621, 0x0627, 0x062D,
                   0x062F, 0x0631, 0x0633, 0x0635, 0x0637, 0x0639,
                   0x0643, 0x0644, 0x0645, 0x0647, 0x0648, 0x0649,
                   0x0640, 0x066E, 0x066F, 0x0660, 0x0661, 0x0662,
                   0x0663, 0x0664, 0x0665, 0x0666, 0x0667, 0x0668,
                   0x0669, 0x06F4, 0x06F5, 0x06F6, 0x06BE, 0x06D2,
                   0x06A9, 0x06AF, 0x06BA, 0x066A, 0x061F, 0x060C,
                   0x061B, 0x066B, 0x066C, 0x066D, 0x064B, 0x064D,
                   0x064E, 0x064F, 0x064C, 0x0650, 0x0651, 0x0652,
                   0x0653, 0x0654, 0x0655, 0x0670, 0x0656, 0x0615,
                   0x0686, 0x0623, 0x0625, 0x0622, 0x0671, 0x0628,
                   0x067E, 0x062A, 0x062B, 0x0679, 0x0629, 0x062C,
                   0x062E, 0x0630, 0x0688, 0x0632, 0x0691, 0x0698,
                   0x0634, 0x0636, 0x0638, 0x063A, 0x0641, 0x0642,
                   0x0646, 0x06D5, 0x06C0, 0x0624, 0x064A, 0x06CC,
                   0x06D3, 0x0626, 0x06C2, 0x06C1, 0x06C3, 0x06F0,
                   0x06F1, 0x06F2, 0x06F3, 0x06F9, 0x06F7, 0x06F8,
                   0xFC63, 0x0672, 0x0673, 0x0675, 0x0676, 0x0677,
                   0x0678, 0x067A, 0x067B, 0x067C, 0x067D, 0x067F,
                   0x0680, 0x0681, 0x0682, 0x0683, 0x0684, 0x0685,
                   0x0687, 0x0689, 0x068A, 0x068B, 0x068C, 0x068D,
                   0x068E, 0x068F, 0x0690, 0x0692, 0x0693, 0x0694,
                   0x0695, 0x0696, 0x0697, 0x0699, 0x069A, 0x069B,
                   0x069C, 0x069D, 0x069E, 0x069F, 0x06A0, 0x06A1,
                   0x06A2, 0x06A3, 0x06A5, 0x06A6, 0x06A7, 0x06A8,
                   0x06AA, 0x06AB, 0x06AC, 0x06AD, 0x06AE, 0x06B0,
                   0x06B1, 0x06B2, 0x06B3, 0x06B4, 0x06B5, 0x06B6,
                   0x06B7, 0x06B8, 0x06B9, 0x06BB, 0x06BC, 0x06BD,
                   0x06BF, 0x06C4, 0x06C5, 0x06CD, 0x06D6, 0x06D7,
                   0x06D8, 0x06D9, 0x06DA, 0x06DB, 0x06DC, 0x06DF,
                   0x06E1, 0x06E2, 0x06E3, 0x06E4, 0x06E5, 0x06E6,
                   0x06E7, 0x06E8, 0x06EA, 0x06EB, 0x06ED, 0x06FB,
                   0x06FC, 0x06FD, 0x06FE, 0x0600, 0x0601, 0x0602,
                   0x0603, 0x060E, 0x060F, 0x0610, 0x0611, 0x0612,
                   0x0613, 0x0614, 0x0657, 0x0658, 0x06EE, 0x06EF,
                   0x06FF, 0x060B, 0x061E, 0x0659, 0x065A, 0x065B,
                   0x065C, 0x065D, 0x065E, 0x0750, 0x0751, 0x0752,
                   0x0753, 0x0754, 0x0755, 0x0756, 0x0757, 0x0758,
                   0x0759, 0x075A, 0x075B, 0x075C, 0x075D, 0x075E,
                   0x075F, 0x0760, 0x0761, 0x0762, 0x0763, 0x0764,
                   0x0765, 0x0766, 0x0767, 0x0768, 0x0769, 0x076A,
                   0x076B, 0x076C, 0x076D, 0x06A4, 0x06C6, 0x06C7,
                   0x06C8, 0x06C9, 0x06CA, 0x06CB, 0x06CF, 0x06CE,
                   0x06D0, 0x06D1, 0x06D4, 0x06FA, 0x06DD, 0x06DE,
                   0x06E0, 0x06E9, 0x060D, 0xFD3E, 0xFD3F, 0x25CC,
                   # Added from https://groups.google.com/d/topic/googlefontdirectory-discuss/MwlMWMPNCXs/discussion
                   0x063b, 0x063c, 0x063d, 0x063e, 0x063f, 0x0620,
                   0x0674, 0x0674, 0x06EC]
        return glyphs

library.register(Charmap)
