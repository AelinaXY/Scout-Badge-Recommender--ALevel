class BadgeList:

    def __init__(self, mapFile):
        import csv   # https://docs.python.org/3.1/library/csv.html
        self.mapList = dict()
        self.mapList['att1'] = dict()
        self.mapList['att2'] = dict()
        self.mapList['att3'] = dict()

        print("MapList:", self.mapList)
        with open(mapFile) as csvfile:
            reader = csv.DictReader(csvfile)
            self.attributeList = reader.fieldnames
            self.badgeList = set()
            try:
                for row in reader:
                    self.mapList["att1"][row['id']] = row['att1']
                    self.mapList["att2"][row['id']] = row['att2']
                    self.mapList["att3"][row['id']] = row['att3']
                    self.badgeList.add(row['id'])
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    def printList(self):
        print("MapList")
        for name in self.attributeList:
            if name in self.mapList:
                print (name, " : ", self.mapList[name])
        for badgeName in self.badgeList:
            print ("Badge: ", badgeName, "\t", self.mapList["att1"][badgeName], ",", self.mapList["att2"][badgeName], ",", self.mapList["att3"][badgeName])
