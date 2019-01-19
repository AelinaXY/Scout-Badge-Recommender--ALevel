class BadgeList:

    def __init__(self, mapFile):
        import csv   # https://docs.python.org/3.1/library/csv.html
        self.mapList = dict()

        with open(mapFile) as csvfile:
            reader = csv.DictReader(csvfile)
            # Copy the array rather than create another reference to it.
            self.attributeList = reader.fieldnames.copy()
            # Drop off the first item ('id')
            self.attributeList.pop(0)
            # Print the attribute list
            # print("AttributeList: ", self.attributeList)
            # Establish empty dictionaries for each attribute type.
            for name in self.attributeList:
                self.mapList[name] = dict()
            self.badgeList = []
            for row in reader:
                self.badgeList.append(row['id']) # Badge Name
                for name in self.attributeList:  # Value of badge attr in dict
                    self.mapList[name][row['id']] = row[name]

    def printList(self):
        print("AttributeList")
        for name in self.attributeList:
            if name in self.mapList:
                print (name, " : ", self.mapList[name])
        for badgeName in self.badgeList:
            print ("Badge: ", badgeName, "\t",
                self.mapList["att1"][badgeName], ",",
                self.mapList["att2"][badgeName], ",",
                self.mapList["att3"][badgeName])
            # Alternate way of doing the above using lists
            print ("Badge: ", badgeName, "\t",
                ",".join(map(lambda x : self.mapList[x][badgeName],
                self.attributeList)))


    def printBadgeList(self):
        print("List of Badges: ",self.badgeList)
