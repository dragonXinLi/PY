from xml.etree import ElementTree

OK = True
main_pid = 10000
loop_depth = 0

# 一.老版本
# 1.新增表，未增加表文件，代码
# 2.新增表，增加表文件，代码
# 3.删除表，未删除表文件，代码
# 4.删除表，删除表文件，代码
# 5.修改表字段，未修改表文件代码字段
# 6.修改表字段，修改表文件代码字段
# 二.新版本

def compare_xml(left, right, key_info='.'):
    global loop_depth
    loop_depth += 1
    if loop_depth == 1: print
    if left.tag != right.tag:
        print_diff(main_pid, key_info, 'difftag', left.tag, right.tag)
        return
    if left.text != right.text:
        print_diff(main_pid, key_info, 'difftext', left.text, right.text)
        return
    leftitems = dict(left.items())
    rightitems = dict(right.items())
    for k, v in leftitems.items():
        if k not in rightitems:
            s = '%s/%s' % (key_info, left.tag)
            print_diff(main_pid, s, 'lostattr', k, "")
    for k, v in rightitems.items():
        if k not in leftitems:
            s = '%s/%s' % (key_info, right.tag)
            print_diff(main_pid, s, 'extraattr', "", k)
    leftnodes = left.getchildren()
    rightnodes = right.getchildren()
    leftlen = len(leftnodes)
    rightlen = len(rightnodes)
    if leftlen != rightlen:
        s = '%s/%s' % (key_info, right.tag)
        print_diff(main_pid, s, 'difflen', leftlen, rightlen)
        return
    l = leftlen < rightlen and leftlen or rightlen
    d = {}
    for i in xrange(l):
        node = leftnodes[i]
        if node.tag not in d:
            d[node.tag] = 1
            tag = node.tag
        else:
            tag = node.tag + str(d[node.tag])
            d[node.tag] += 1
        s = '%s/%s' % (key_info, tag)
        compare_xml(leftnodes[i], rightnodes[i], s)

def compare_xml2(left, right, key_info='.'):
    leftnodes = left.getchildren()
    rightnodes = right.getchildren()
    leftlen = len(leftnodes)
    rightlen = len(rightnodes)
    if leftlen != rightlen:
        print "新增表结构"

def print_diff(main_pid, key_info, msg, base_type, test_type):
    global OK
    info = u'[ %-5s ] %s -> %-40s [ %s != %s ]' % (msg.upper(), main_pid, key_info.strip('./'), base_type, test_type)
    print info.encode('gbk')
    OK = False


if __name__ == '__main__':
    s1 = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<model type="com.apple.IDECoreDataModeler.DataModel" documentVersion="1.0" lastSavedToolsVersion="14133" systemVersion="17E199" minimumToolsVersion="Automatic" sourceLanguage="Objective-C" userDefinedModelVersionIdentifier="">
    <entity name="Reminder" representedClassName="Reminder" syncable="YES" syncableeeee="YES">
        <attribute name="time" optional="YES" attributeType="Date" usesScalarValueType="NO" syncable="YES"/>
        <relationship name="student" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Student" inverseName="reminders" inverseEntity="Student" syncable="YES"/>
        <relationship name="teacher" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Teacher" inverseName="reminders" inverseEntity="Teacher" syncable="YES"/>
    </entity>
    <entity name="Student" representedClassName="Student" syncable="YES">
        <attribute name="age" optional="YES" attributeType="Integer 16" defaultValueString="0" usesScalarValueType="NO" syncable="YES"/>
        <attribute name="name" optional="YES" attributeType="String" syncable="YES"/>
        <relationship name="reminders" optional="YES" toMany="YES" deletionRule="Cascade" destinationEntity="Reminder" inverseName="student" inverseEntity="Reminder" syncable="YES"/>
        <relationship name="teacher" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Teacher" inverseName="students" inverseEntity="Teacher" syncable="YES"/>
    </entity>
    <entity name="Teacher" representedClassName="Teacher" syncable="YES">
        <attribute name="age" optional="YES" attributeType="Integer 16" defaultValueString="0" usesScalarValueType="NO" syncable="YES"/>
        <attribute name="name" optional="YES" attributeType="String" syncable="YES"/>
        <relationship name="reminders" optional="YES" toMany="YES" deletionRule="Cascade" destinationEntity="Reminder" inverseName="teacher" inverseEntity="Reminder" syncable="YES"/>
        <relationship name="students" optional="YES" toMany="YES" deletionRule="Nullify" destinationEntity="Student" inverseName="teacher" inverseEntity="Student" syncable="YES"/>
    </entity>
    <elements>
        <element name="Reminder" positionX="0" positionY="45" width="128" height="90"/>
        <element name="Student" positionX="27" positionY="72" width="128" height="105"/>
        <element name="Teacher" positionX="-36" positionY="9" width="128" height="105"/>
    </elements>
</model>'''

    s2 = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<model type="com.apple.IDECoreDataModeler.DataModel" documentVersion="1.0" lastSavedToolsVersion="14135" systemVersion="17E199" minimumToolsVersion="Automatic" sourceLanguage="Objective-C" userDefinedModelVersionIdentifier="">
    <entity name="Reminder" representedClassName="Reminder" syncable="YES">
        <attribute name="time" optional="YES" attributeType="Date" usesScalarValueType="NO" syncable="YES"/>
        <relationship name="student" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Student" inverseName="reminders" inverseEntity="Student" syncable="YES"/>
        <relationship name="teacher" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Teacher" inverseName="reminders" inverseEntity="Teacher" syncable="YES"/>
    </entity>
    <entity name="Student" representedClassName="Student" syncable="YES">
        <attribute name="age" optional="YES" attributeType="Integer 16" defaultValueString="0" usesScalarValueType="NO" syncable="YES"/>
        <attribute name="name" optional="YES" attributeType="String" syncable="YES"/>
        <relationship name="reminders" optional="YES" toMany="YES" deletionRule="Cascade" destinationEntity="Reminder" inverseName="student" inverseEntity="Reminder" syncable="YES"/>
        <relationship name="teacher" optional="YES" maxCount="1" deletionRule="Nullify" destinationEntity="Teacher" inverseName="students" inverseEntity="Teacher" syncable="YES"/>
    </entity>
    <entity name="Teacher" representedClassName="Teacher" syncable="YES">
        <attribute name="age" optional="YES" attributeType="Integer 16" defaultValueString="0" usesScalarValueType="NO" syncable="YES"/>
        <attribute name="name" optional="YES" attributeType="String" syncable="YES"/>
        <relationship name="reminders" optional="YES" toMany="YES" deletionRule="Cascade" destinationEntity="Reminder" inverseName="teacher" inverseEntity="Reminder" syncable="YES"/>
        <relationship name="students" optional="YES" toMany="YES" deletionRule="Nullify" destinationEntity="Student" inverseName="teacher" inverseEntity="Student" syncable="YES"/>
    </entity>
    <elements>
        <element name="Reminder" positionX="0" positionY="45" width="128" height="90"/>
        <element name="Student" positionX="27" positionY="72" width="128" height="105"/>
        <element name="Teacher" positionX="-36" positionY="9" width="128" height="105"/>
    </elements>
</model>'''
    lroot = ElementTree.fromstring(s1)
    rroot = ElementTree.fromstring(s2)
    compare_xml(lroot, rroot)
