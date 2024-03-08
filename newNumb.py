class nb:
    def __init__(self, v):
        self.v = v
        self.path = str(v)

    def __add__(self, o):
        a = nb(self.v + o.v)
        a.path = ""
        a.path = " "+ self.path + " + " + o.path + " "
        return a


    def __mul__(self, o):
        a = nb(self.v * o.v)
        a.path = ""
        if " " in self.path :
            a.path += "(" + self.path + ")"
        else:
            a.path += " "+self.path+" "

        a.path += " * "
        if " " in o.path :
            a.path += "(" + o.path + ")"
        else:
            a.path += " "+o.path+" "
        return a


    def __sub__(self, o):
        a = nb(self.v - o.v)
        a.path = ""
        if " " in self.path :
            a.path += "(" + self.path + ")"
        else:
            a.path += self.path

        a.path += " - "
        if " " in o.path :
            a.path += "(" + o.path + ")"
        else:
            a.path += " "+o.path+" "
        return a


    def __floordiv__(self, o):
        a = nb(self.v // o.v)
        a.path = ""
        if " " in self.path :
            a.path += "_(_" + self.path + "_)_"
        else:
            a.path += " " + self.path + " "

        a.path += " / "
        if " " in o.path :
            a.path += "(" + o.path + ")"
        else:
            a.path += " "+o.path+" "
        return a


    def __lt__(self, o):
        if type(o)==nb:
            return self.v < o.v
        else:
            return self.v < o

    def __gt__(self, o):
        if type(o)==nb:
            return self.v > o.v
        else:
            return self.v > o

    def __le__(self, o):
        if type(o)==nb:
            return self.v <= o.v
        else:
            return self.v <= o

    def __ge__(self, o):
        if type(o)==nb:
            return self.v >= o.v
        else:
            return self.v >= o

    def __mod__(self, o):
        return self.v % o.v

    def __str__(self):
        return str(self.v)

    def __repr__(self):
        return str(self.v)

    def __eq__(self, o):
        if(type(o) == nb):
            return self.v == o.v
        else:
            return self.v == o

    def __ne__(self,o):
        return not self.__eq__(o)
