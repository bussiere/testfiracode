import fontforge
font = fontforge.open('firacode.ttf')
shield = font.createChar(128737)
shield.importOutlines('shield.svg')
#crossbone = font.createChar(9760)
#crossbone.importOutlines('crossbone.svg')
font.addLookup('crossbone', 'gsub_single', (), (('liga', (('DFLT', ('dflt')),)),))
font.addLookupSubtable('crossbone', 'crossbone')
font[9760].addPosSub('crossbone', "9760")
font.addLookup('shield', 'gsub_single', (), (('liga', (('DFLT', ('dflt')),)),))
font.addLookupSubtable('shield', 'shield')
font[128737].addPosSub('shield', "128737")
#font[128737] = shield
font.fullname = 'FiraCodeEmojii'
font.familyname = 'FiraCode'
font.fontname = 'FiraCodeEmojii'
font.uniqueid = 123456789
font.xuid = '123456789'
font.appendSFNTName('English (US)', 'SubFamily', "FiraCodeEmojii SemiBold Italic")
font.appendSFNTName('English (US)', 'Fullname', "FiraCodeEmojii SemiBold Italic")
font.appendSFNTName('English (US)', 'Preferred Family', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Preferred Styles', "SemiBold Italic")
font.appendSFNTName('English (US)', 'Compatible Full', "FiraCodeEmojii SemiBold Italic")
font.appendSFNTName('English (US)', 'WWS Family', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'WWS Subfamily', "SemiBold Italic")
font.appendSFNTName('English (US)', 'Sample Text', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Trademark', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Manufacturer', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Designer', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Vendor URL', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Designer URL', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'License', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'License URL', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'UniqueID', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Preferred Family', "FiraCodeEmojii")
font.appendSFNTName('English (US)', 'Preferred Styles', "SemiBold Italic")
font.appendSFNTName('English (US)', 'Compatible Full', "FiraCodeEmojii SemiBold Italic")
font.reencode('unicode')
font.generate('testtfont.ttf')