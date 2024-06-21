import json
import os.path

import numpy as np
import lxml.etree as ET
from lxml.etree import Element, SubElement, tostring





class MTRANS():
    def __init(self):
        super().__init__()

    def __is_contain_chinese(self, path):
        for char in path:
            if '\u4e00' <= char <= '\u9fff':
                return True
        return False

    def __is_elements_all_num(self, lst):
        for elem in lst:
            if type(elem) not in [int]:
                return False
        return True

    def __is_elements_all_str(self, lst):
        for elem in lst:
            if type(elem) not in [str]:
                return False
        return True

    def __xyxy2xywh(self, xmin, ymin, xmax, ymax):
        """
        转换单个框到yolo格式
        """
        w = xmax - xmin
        h = ymax - ymin
        x = (xmin + xmax) / 2.0
        y = (ymin + ymax) / 2.0
        return (x, y, w, h)

    def __xyxy2xywhn(self, xmin, ymin, xmax, ymax, W, H):
        """
        转换单个框到yolo格式
        """
        dw = 1. / W
        dh = 1. / H
        w = (xmax - xmin) * dw
        h = (ymax - ymin) * dh
        x = (xmin + xmax) * dw / 2.0
        y = (ymin + ymax) * dh / 2.0
        return (x, y, w, h)

    def __xywhn2xyxy(self, x_center, y_center, w, h, W, H):
        """
        转换单个框到yolo格式
        """
        x_center *= W
        y_center *= H
        w *= W
        h *= H
        xmin, xmax = int(x_center - w / 2.), int(x_center + w / 2.)
        ymin, ymax = int(y_center - h / 2.), int(y_center + h / 2.)
        return (xmin, ymin, xmax, ymax)

    def __xywhangle2xyxyxyxy(self, cx, cy, w, h, angle):
        angle = -angle  # 这里是图像坐标
        points = [[cx - w / 2, cy - h / 2], [cx + w / 2, cy - h / 2],
                  [cx + w / 2, cy + h / 2], [cx - w / 2, cy + h / 2]]
        newpoints = []
        if angle < 0:  # 逆时针
            angle = -angle
            for point in points:
                x, y = point
                newx = round((x - cx) * np.cos(angle) - (y - cy) * np.sin(angle) + cx, 1)
                newy = round((x - cx) * np.sin(angle) + (y - cy) * np.cos(angle) + cy, 1)
                newpoints.append([newx, newy])
        else:
            for point in points:
                x, y = point
                newx = round((x - cx) * np.cos(angle) + (y - cy) * np.sin(angle) + cx, 1)
                newy = round((y - cy) * np.cos(angle) - (x - cx) * np.sin(angle) + cy, 1)
                newpoints.append([newx, newy])
        return newpoints

    def labels2dict(self, labels, idxs):
        assert (type(labels) == list or type(labels) == tuple), "labels(参数1)必须为数组或列表格式!!!"
        assert (type(idxs) == list or type(idxs) == tuple), "idxs(参数2)必须为列表或数组格式!!!"
        assert (len(labels) == len(idxs)), "labels(参数1)和idxs(参数2)个数不对应,请检查!!!"
        assert (len(set(labels)) == len(labels)), "labels(参数1)有重复,请检查!!!"
        assert (len(set(idxs)) == len(idxs)), "idxs(参数2)有重复,请检查!!!"
        assert (self.__is_elements_all_str(idxs)), "idxs(参数2)中必须为数字字符串'0','1'!!!"
        assert (self.__is_elements_all_str(labels)), "label(参数1)中必须为字符串"
        names = {}
        for i in range(len(labels)):
            names[labels[i]] = idxs[i]
        return names

    def voc2yolo(self, path_xml: str, path_txt: str, namedict: dict):
        """
        :param path_xml: xml 标注文件地址
        :param path_txt: 保存的yolo格式文件地址
        :param namelist: 标签的名字与对应的label_id组成的字典
        """
        tree = ET.parse(path_xml)
        root = tree.getroot()
        size = root.find('size')
        W = int(size.find('width').text)
        H = int(size.find('height').text)
        assert (W>0 and H>0), "检查xml格式，标注错误，检查xml文件中width与height大小！！！"
        txt = open(path_txt, 'w')
        if (root.find('object') == None):
            txt.close()
            return 0
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in namedict.keys():
                continue
            label = str(namedict[cls])
            xmlbox = obj.find('bndbox')
            xmin, xmax, ymin, ymax = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                                      float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            x, y, w, h = self.__xyxy2xywhn(xmin, ymin, xmax, ymax, W, H)
            txt.write(label + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")
        txt.close()
        return 1

    def voc2dotaobb(self, path_xml: str, path_txt: str):
        """
        :param path_xml: xml 标注文件地址
        :param path_txt: 保存的yolo格式文件地址
        """

        tree = ET.parse(path_xml)
        root = tree.getroot()
        size = root.find('size')
        W = int(size.find('width').text)
        H = int(size.find('height').text)
        assert (W>0 and H>0), "检查xml格式，标注错误，检查xml文件中width与height大小！！！"
        txt = open(path_txt, 'w')
        if (root.find('object') == None):
            txt.close()
            return 0
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            if (obj.find('type').text == 'robndbox'):
                cls = obj.find('name').text
                xmlbox = obj.find('robndbox')
                cx, cy, w, h, angle = (float(xmlbox.find('cx').text), float(xmlbox.find('cy').text),
                                       float(xmlbox.find('w').text), float(xmlbox.find('h').text),
                                       float(xmlbox.find('angle').text))
                newpoints = self.__xywhangle2xyxyxyxy(cx, cy, w, h, angle)  # 计算旋转后的4个点坐标
            elif (obj.find('type').text == 'bndbox'):
                cls = obj.find('name').text
                xmlbox = obj.find('bndbox')
                xmin, ymin, xmax, ymax = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                                          float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
                cx, cy, w, h = self.__xyxy2xywh(xmin, ymin, xmax, ymax)
                newpoints = self.__xywhangle2xyxyxyxy(cx, cy, w, h, 0)  # 计算旋转后的4个点坐标
            newpoints = np.array(newpoints)
            newpoints = newpoints.astype(int)
            line = ''
            for point in newpoints:
                line += str(point[0]) + ' ' + str(point[1]) + ' '
            line += cls + ' ' + difficult +'\n'
            txt.write(line)
        txt.close()
        return 1

    def voc2yoloobb(self, path_xml: str, path_txt: str, namedict: dict):
        """
        :param path_xml: xml 标注文件地址
        :param path_txt: 保存的yolo格式文件地址
        """
        tree = ET.parse(path_xml)
        root = tree.getroot()
        size = root.find('size')
        W = int(size.find('width').text)
        H = int(size.find('height').text)
        assert (W>0 and H>0), "检查xml格式，标注错误，检查xml文件中width与height大小！！！"
        txt = open(path_txt, 'w')
        if (root.find('object') == None):
            txt.close()
            return 0
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in namedict.keys():
                continue
            if (obj.find('type').text == 'robndbox'):
                xmlbox = obj.find('robndbox')
                cx, cy, w, h, angle = (float(xmlbox.find('cx').text), float(xmlbox.find('cy').text),
                                       float(xmlbox.find('w').text), float(xmlbox.find('h').text),
                                       float(xmlbox.find('angle').text))
                newpoints = self.__xywhangle2xyxyxyxy(cx, cy, w, h, angle)  # 计算旋转后的4个点坐标
            elif (obj.find('type').text == 'bndbox'):
                xmlbox = obj.find('bndbox')
                xmin, ymin, xmax, ymax = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                                          float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
                cx, cy, w, h = self.__xyxy2xywh(xmin, ymin, xmax, ymax)
                newpoints = self.__xywhangle2xyxyxyxy(cx, cy, w, h, 0)  # 计算旋转后的4个点坐标
            newpoints = np.array(newpoints)
            newpoints = newpoints.astype(int)
            line = str(namedict[cls]) + " "
            for point in newpoints:
                line += str(point[0]/W) + ' ' + str(point[1]/H) + ' '
            line += '\n'
            txt.write(line)
        txt.close()
        return 1

    def json2yolo(self, path_json: str, path_txt: str, namedict: dict, mode="detection"):
        """
        :param path_xml: xml 标注文件地址
        :param path_txt: 保存的yolo格式文件地址
        :param namelist: 标签的名字与对应的label_id组成的字典
        """
        assert (mode == "segmentation" or mode == "detection"), "不存在当前的转换类型:" + str(mode)
        f = open(path_json, 'r', encoding="utf-8")
        data = json.load(f)
        f.close()
        H = int(data["imageHeight"])
        W = int(data["imageWidth"])
        assert (W>0 and H>0), "检查xml格式，标注错误，检查xml文件中width与height大小！！！"
        txt = open(path_txt, 'w')
        shapes = data["shapes"]
        if mode == "segmentation":
            for shape in shapes:
                points = shape["points"]
                if shape["label"] in namedict.keys():
                    label = str(namedict[shape["label"]])
                    txt.write(label)
                    for point in points:
                        x = float(point[0]) / W
                        y = float(point[1]) / H
                        txt.write(" " + str(x) + " " + str(y))
                    txt.write("\n")
        elif mode == "detection":
            for shape in shapes:
                points = shape["points"]
                if shape["label"] in namedict.keys():
                    label = str(namedict[shape["label"]])
                    txt.write(label)
                    x_ = []
                    y_ = []
                    for point in points:
                        x_.append(float(point[0]))
                        y_.append(float(point[1]))
                    x_max, x_min = max(x_), min(x_)
                    y_max, y_min = max(y_), min(y_)
                    x, y, w, h = self.__xyxy2xywhn(x_min, y_min, x_max, y_max, W, H)
                    txt.write(" " + str(x) + " " + str(y) + " " + str(w) + " " + str(h))
                    txt.write("\n")
        txt.close()
        if(len(shapes)==0):
            return 0
        return 1

    def yolo2voc(self, path_img, path_txt, path_xml, namedict):
        """
        :param path_img: 图像位置
        :param path_txt: yolo标注格式文件地址
        :param path_txt: 需要保存的xml标注格式文件地址
        :param namelist: 标签的名字与对应的label_id组成的字典
        """
        import cv2
        img = cv2.imread(path_img, 1)
        H, W, C = img.shape
        root = Element('annotation')
        img_n = os.path.basename(path_img)
        img_f = os.path.basename(os.path.dirname(path_img))
        folder = SubElement(root, 'folder')
        folder.text = img_f
        filename= SubElement(root, 'filename')
        filename.text = img_n
        path = SubElement(root, 'path')
        path.text = path_img
        source = SubElement(root, 'source')
        folder = SubElement(source, 'database')
        folder.text = "Unknown"
        size = SubElement(root, 'size')
        width, height, depth = SubElement(size, 'width'), SubElement(size, 'height'), SubElement(size, 'depth')
        width.text, height.text, depth.text = str(W), str(H), str(C)
        segmented = SubElement(root, 'segmented')
        segmented.text = '0'
        #以上写的是基础
        f = open(path_txt, 'r')
        lines = f.readlines()
        f.close()
        if (len(lines)==0):
            tree = ElementTree(root)
            tree.write(path_xml)
            return 0
        for line in lines:
            line = line.replace('\r', '')
            line = line.strip()
            linelist = line.split(' ')
            assert (len(linelist)==5), "检查格式，可能不是常规的label x y w h 格式！！！"
            idx, x, y, w, h = linelist
            if idx not in namedict.keys():
                continue
            label = namedict[idx]
            x_min, y_min, x_max, y_max = self.__xywhn2xyxy(float(x), float(y), float(w), float(h), W, H)
            obj = SubElement(root, 'object')
            name = SubElement(obj, 'name')
            name.text = label
            pose = SubElement(obj, 'pose')
            pose.text = 'Unspecified'
            truncated = SubElement(obj, 'truncated')
            truncated.text = '0'
            difficult = SubElement(obj, 'difficult')
            difficult.text = '0'
            bndbox = SubElement(obj, 'bndbox')
            xmin, ymin = SubElement(bndbox, 'xmin'), SubElement(bndbox, 'ymin')
            xmax, ymax = SubElement(bndbox, 'xmax'), SubElement(bndbox, 'ymax')
            xmin.text, ymin.text, xmax.text, ymax.text = str(x_min), str(y_min), str(x_max), str(y_max)
        xml = tostring(root, pretty_print=True)  # 格式化显示，该换行的换行
        file_object = open(path_xml, 'wb')
        file_object.write(xml)
        file_object.close()
        return 0








Mtrans = MTRANS()