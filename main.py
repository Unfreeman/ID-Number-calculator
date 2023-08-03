IDNumber = "110101********1024"
IDN_list = [IDNumber]

save_path = "save"

year_from = 1900
year_to = 2035
month_from = 1
month_to = 12
day_from = 1
day_to = 31


def possible(list_in):
    if "*" in str(list_in):
        list_out = []
        for item in list_in:
            for i in range(0, 10):
                item_rpl = item.replace("*", str(i), 1)
                list_out.append(item_rpl)
        return possible(list_out)
    else:
        return list_in


provinces_lst = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41", "42",
                 "43", "44", "45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65", "71", "81", "82",
                 "83"]

vrf_coef = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]


def legal(str_in):
    part_main = str_in[0:17]
    part_vrf = str_in[17]
    sum = 0
    for i in range(0, 17):
        sum += int(part_main[i]) * vrf_coef[i]
    vrf_num = 0
    if part_vrf == "X" or part_vrf == "x":
        vrf_num = 10
    else:
        vrf_num = int(part_vrf)
    if (12 - sum % 11) % 11 == vrf_num:
        return True
    else:
        return False


mo_dy_list = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def datechk(ymd):
    yr = int(ymd[0:4])
    mo = int(ymd[4:6])
    dy = int(ymd[6:8])
    if yr in range(year_from, year_to + 1) and mo in range(month_from, month_to + 1) and dy in range(day_from,
                                                                                                     day_to + 1):
        if dy <= mo_dy_list[mo]:
            return True
        elif mo == 2 and dy == 29:
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def exist_chk(list_in):
    list_out = []
    for item in list_in:
        if item[0:2] in provinces_lst and int(item[2:4]) <= 70:
            if datechk(item[6:14]):
                if legal(item):
                    list_out.append(item)
    return list_out


result = exist_chk(possible(IDN_list))

with open(save_path, "wt") as out_file:
    out_file.write(str(result))
    print(result)
    sum = 0
    for i in result:
        sum += 1
    print(sum)
