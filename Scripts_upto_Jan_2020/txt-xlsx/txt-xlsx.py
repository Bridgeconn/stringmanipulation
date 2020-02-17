# -*- coding: utf-8 -*-
import os
import glob
from openpyxl import Workbook
import openpyxl
T_filePath = glob.glob(os.getcwd() + '/' + 'newfolder' + '/')
# print(T_filePath)

heading = [ 
"​1. Creation and God",
"2. Creation and Us",
"3. The Fall",
"4. The Flood",
"5. Abraham’s Covenant",
"6. Joseph",
"7. Moses and the Plagues",
"8. The Ten Commandments",
"9. Presence of God",
"10. The Holiness of God (Leviticus)",
"11. Sold Out to God (Deuteronomy)",
"12. Judges",
"13. God is King (1 Samuel)",
"14. David and Goliath",
"15. Psalm 23",
"16. Confrontation and Confession (Psalm 51)",	
"17. Solomon — the Wise and Foolish (Proverbs)",
"18. Job",
"19. Elijah",
"20. Isaiah and the Holiness of God",
"21. Isaiah 53",
"22. Micah",
"23. Hosea",
"24. Habakkuk, Righteousness and Faith",
"25. The New Covenant (Jeremiah and Ezekiel)",
"26. Lamentations",
"27. The Birth of Jesus",
"28. John the Baptist",
"29. Nicodemus and Rebirth",
"30. The Beatitudes",
"31. The Lord’s Prayer",
"32. Seeking God",
"33. Deity of Christ",
"34. Discipleship",
"35. The Greatest Commandment",
"36. Eschatology",
"37. Holy Spirit",
"38. The Lord’s Supper",
"39. Jesus’ Death and Resurrection",
"40. The Great Commission",
"41. Pentecost",
"42. The Church",
"43. Justification by Faith",
"44. The Grace of Giving",
"45. Christian Joy",
"46. Humility",
"47. Scripture",
"48. Assurance and Perseverance (Hebrews)",
"49. The Tongue (James)",
"50. Suffering and Heaven",
"51. Christian Love",
"52. Revelation" 
]


f = open("52stories.txt", "r")
content = f.read()
split_content = content.split("\n")
translation = " "

for lines in split_content:
    if lines in heading:
        xlxbook = Workbook()
        sheet = xlxbook.active
        splitLines = lines.split('.')[0]
        print(splitLines)
        sheet.append(("ENGLISH","TRANSLATION"))
        xlxbook.save(T_filePath[0]+"Chapter"+splitLines+'.xlsx')
    else:
        # print(lines)
        wbk = openpyxl.load_workbook(T_filePath[0]+"Chapter"+splitLines+'.xlsx')
        sheet1 = wbk.active
        sheet1.append((lines,translation))
        wbk.save(T_filePath[0]+"Chapter"+splitLines+'.xlsx')
        wbk.close
    
        


        # print(lines)
