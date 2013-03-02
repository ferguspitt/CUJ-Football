#Produce A list of score permutations 

list2Perm = ["1","2","3","4","5","6","7","8","9","10","1","2","3","4","5","6","7","8","9","10",]
listDashPerm = [[a+" - "+b]
            for a in list2Perm
            for b in list2Perm
            ]
listDshPerm = [[a+"-"+b]
            for a in list2Perm
            for b in list2Perm
            ]
listSlashPerm = [[a+" / "+b]
            for a in list2Perm
            for b in list2Perm
            ]
listSlshPerm = [[a+"/"+b]
            for a in list2Perm
            for b in list2Perm
            ]
listAllPerms = [listDashPerm + listDshPerm + listSlashPerm + listSlshPerm]