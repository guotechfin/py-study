#!/bin/env python
# -*- coding:utf8 -*-


from wood_model import Wood
from common import utility


class WoodService(object):
    def search_wood_list(
            self,
            session,
            wood_id=-1,
            start=-1,
            end=-1,
            like_name="",
            like_size="",
            flag=0):
        wood = session.query(Wood)
        if wood_id != -1:
            wood = wood.filter_by(id=wood_id)
        if like_name != "":
            wood = wood.filter(Wood.name.like("%%%s%%" % like_name))
        if like_size != "":
            wood = wood.filter(Wood.size.like("%%%s%%" % like_size))
        if flag != -1:
            wood = wood.filter_by(flag=flag)
        if start == -1 and end == -1:
            return wood.all()
        else:
            return wood[start:end], wood.count()

    def make_volumn(self, length, width, heigth, number):
        return length * width * heigth * number / 1000000

    def make_size(self, length, width, heigth):
        return "%s*%s*%s" % (length, width, heigth)

    def new_wood(
            self,
            session,
            name="",
            length=0,
            width=0,
            heigth=0,
            number=1,
            grade=""):
        wood = Wood(name=name.strip(),
                length=length,
                width=width,
                heigth=heigth,
                number=number,
                grade=grade.strip(),
                volumn=self.make_volumn(length, width, heigth, number),
                size=self.make_size(length, width, heigth),
                remain=0)
        session.add(wood)

    def modify_wood(
            self,
            session,
            wood_id,
            name="",
            length=0,
            width=0,
            heigth=0,
            number=1,
            grade=""):
        data = dict()
        data['name'] = name.strip()
        data['length'] = length
        data['width'] = width
        data['heigth'] = heigth
        data['number'] = number
        data['volumn'] = self.make_volumn(length, width, heigth, number)
        data['grade'] = grade.strip()
        data['size'] = self.make_size(length, width, heigth)
        session.query(Wood).filter_by(id=wood_id).update(data)

    def update_wood_remain(self, session, wood_id, remain, type=0):
        wood = session.query(Wood).filter_by(id=wood_id)
        if type == 0:
            wood.update({Wood.remain: remain})
        elif type == 1:
            wood.update({Wood.remain: Wood.remain + remain})
        elif type == 2:
            wood.update({Wood.remain: Wood.remain - remain})

    def del_wood(self, session, wood_id):
        session.query(Wood).filter_by(id=wood_id).update({Wood.flag: 1})


wood_obj = WoodService()
