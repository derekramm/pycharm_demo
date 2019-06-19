import datetime
import random

first_names = ['李', '王', '张', '刘', '陈', '杨', '黄', '赵', '周', '吴', '徐', '孙', '朱', '马', '胡', '郭', '林', '何', '高', '梁', '郑',
               '罗', '宋', '谢', '唐', '韩', '曹', '许', '邓', '萧', '冯', '曾', '程', '蔡', '彭', '潘', '袁', '于', '董', '余', '苏', '叶',
               '吕', '魏', '蒋', '田', '杜', '丁', '沈', '姜', '范', '江', '傅', '钟', '卢', '汪', '戴', '崔', '任', '陆', '廖', '姚', '方',
               '金', '邱', '夏', '谭', '韦', '贾', '邹', '石', '熊', '孟', '秦', '阎', '薛', '侯', '雷', '白', '龙', '段', '郝', '孔', '邵',
               '史', '毛', '常', '万', '顾', '赖', '武', '康', '贺', '严', '尹', '钱', '施', '牛', '洪', '龚', '汤', '陶', '黎', '温', '莫',
               '易', '樊', '乔', '文', '安', '殷', '颜', '庄', '章', '鲁', '倪', '庞', '邢', '俞', '翟', '蓝', '聂', '齐', '向', '申', '葛',
               '岳']
boy_last_names = ['澄邈', '德泽', '海超', '海阳', '海荣', '海逸', '海昌', '瀚钰', '瀚文', '涵亮', '涵煦', '涵蓄', '涵衍', '浩皛', '浩波', '浩博', '浩初',
                  '浩宕', '浩歌', '浩广', '浩邈', '浩气', '浩思', '浩言', '鸿宝', '鸿波', '鸿博', '鸿才', '鸿畅', '鸿畴', '鸿达', '鸿德', '鸿飞', '鸿风',
                  '鸿福', '鸿光', '鸿晖', '鸿朗', '鸿文', '鸿轩', '鸿煊', '鸿骞', '鸿远', '鸿云', '鸿哲', '鸿祯', '鸿志', '鸿卓', '嘉澍', '光济', '澎湃',
                  '彭泽', '鹏池', '鹏海', '浦和', '浦泽', '瑞渊', '越泽', '博耘', '德运', '辰宇', '辰皓', '辰钊', '辰铭', '辰锟', '辰阳', '辰韦', '辰良',
                  '辰沛', '晨轩', '晨涛', '晨濡', '晨潍', '鸿振', '吉星', '铭晨', '起运', '运凡', '运凯', '运鹏', '运浩', '运诚', '运良', '运鸿', '运锋',
                  '运盛', '运升', '运杰', '运珧', '运骏', '运凯', '运乾', '维运', '运晟', '运莱', '运华', '耘豪', '星爵', '星腾', '星睿', '星泽', '星鹏',
                  '星然', '震轩', '震博', '康震', '震博', '振强', '振博', '振华', '振锐', '振凯', '振海', '振国', '振平', '昂然', '昂雄', '昂杰', '昂熙',
                  '昌勋', '昌盛', '昌淼', '昌茂', '昌黎', '昌燎', '昌翰', '晨朗', '德明', '德昌', '德曜', '范明', '飞昂', '高旻', '晗日', '昊然', '昊天',
                  '昊苍', '昊英', '昊宇', '昊嘉', '昊明', '昊伟', '昊硕', '昊磊', '昊东', '鸿晖', '鸿朗', '华晖', '金鹏', '晋鹏', '敬曦', '景明', '景天',
                  '景浩', '俊晖', '君昊', '昆琦', '昆鹏', '昆纬', '昆宇', '昆锐', '昆卉', '昆峰', '昆颉', '昆谊', '昆皓', '昆鹏', '昆明', '昆杰', '昆雄',
                  '昆纶', '鹏涛', '鹏煊', '曦晨', '曦之', '新曦', '旭彬', '旭尧', '旭鹏', '旭东', '旭炎', '炫明', '宣朗', '学智', '轩昂', '彦昌', '曜坤',
                  '曜栋', '曜文', '曜曦', '曜灿', '曜瑞', '智伟', '智杰', '智刚', '智阳', '昌勋', '昌盛', '昌茂', '昌黎', '昌燎', '昌翰', '晨朗', '昂然',
                  '昂雄', '昂杰', '昂熙', '范明', '飞昂', '高朗', '高旻', '德明', '德昌', '德曜', '智伟', '智杰', '智刚', '智阳', '瀚彭', '旭炎', '宣朗',
                  '学智', '昊然', '昊天', '昊苍', '昊英', '昊宇', '昊嘉', '昊明', '昊伟', '鸿朗', '华晖', '金鹏', '晋鹏', '敬曦', '景明', '景天', '景浩',
                  '景行', '景中', '景逸', '景彰', '昆鹏', '昆明', '昆杰', '昆雄', '昆纶', '鹏涛', '鹏煊', '景平', '俊晖', '君昊', '昆琦', '昆鹏', '昆纬',
                  '昆宇', '昆锐', '昆卉', '昆峰', '昆颉', '昆谊', '轩昂', '彦昌', '曜坤', '曜文', '曜曦', '曜灿', '曜瑞', '曦晨', '曦之', '新曦', '鑫鹏',
                  '旭彬', '旭尧', '旭鹏', '旭东', '浩轩', '浩瀚', '浩慨', '浩阔', '鸿熙', '鸿羲', '鸿禧', '鸿信', '泽洋', '泽雨', '哲瀚', '胤运', '佑运',
                  '允晨', '运恒', '运发', '云天', '耘志', '耘涛', '振荣', '振翱', '中震', '子辰', '晗昱', '瀚玥', '瀚昂', '瀚彭', '景行', '景中', '景逸',
                  '景彰', '绍晖', '文景', '曦哲', '永昌', '子昂', '智宇', '智晖', '晗日', '晗昱', '瀚昂', '昊硕', '昊磊', '昊东', '鸿晖', '绍晖', '文昂',
                  '文景', '曦哲', '永昌', '子昂', '智宇', '智晖', '浩然', '鸿运', '辰龙', '运珹', '振宇', '高朗', '景平', '鑫鹏', '昌淼', '炫明', '昆皓',
                  '曜栋', '文昂']
girl_last_names = ['恨桃', '依秋', '依波', '香巧', '紫萱', '涵易', '忆之', '幻巧', '水风', '安寒', '白亦', '惜玉', '碧春', '怜雪', '听南', '念蕾', '紫夏',
                   '凌旋', '芷梦', '凌寒', '梦竹', '千凡', '采波', '元冬', '思菱', '平卉', '笑柳', '雪卉', '南蓉', '谷梦', '巧兰', '绿蝶', '飞荷', '平安',
                   '芷荷', '怀瑶', '慕易', '若芹', '紫安', '曼冬', '寻巧', '寄波', '尔槐', '以旋', '初夏', '依丝', '怜南', '傲菡', '谷蕊', '笑槐', '飞兰',
                   '笑卉', '迎荷', '元冬', '痴安', '妙绿', '觅雪', '寒安', '沛凝', '白容', '乐蓉', '映安', '依云', '映冬', '凡雁', '梦秋', '梦凡', '秋巧',
                   '若云', '元容', '怀蕾', '灵寒', '天薇', '翠安', '乐琴', '宛南', '怀蕊', '白风', '访波', '亦凝', '易绿', '夜南', '曼凡', '亦巧',
                   '青易。冰真', '白萱', '友安', '海之', '小蕊', '又琴', '天风', '若松', '盼菡', '秋荷', '香彤', '语梦', '惜蕊', '迎彤', '沛白', '雁山',
                   '易蓉', '雪晴', '诗珊', '春冬', '又绿', '冰绿', '半梅', '笑容', '沛凝', '映秋', '盼烟', '晓凡', '涵雁', '问凝', '冬萱', '晓山', '雁蓉',
                   '梦蕊', '山菡', '南莲', '飞双', '凝丝', '思萱', '怀梦', '雨梅', '冷霜', '向松', '迎丝', '迎梅', '雅彤', '香薇', '以山', '碧萱', '寒云',
                   '向南', '书雁', '怀薇', '思菱', '忆文', '翠巧', '怀山', '若山', '向秋', '凡白', '绮烟', '从蕾', '天曼', '又亦', '从安', '绮彤', '之玉',
                   '凡梅', '依琴', '沛槐', '又槐', '元绿', '安珊', '夏之', '易槐', '宛亦', '白翠', '丹云', '问寒', '易文', '傲易', '青旋', '思真', '雨珍',
                   '幻丝', '代梅', '盼曼', '妙之', '半双', '若翠', '初兰', '惜萍', '初之', '宛丝', '寄南', '小萍', '静珊', '千风', '天蓉', '雅青', '寄文',
                   '涵菱', '香波', '青亦', '元菱', '翠彤', '春海', '惜珊', '向薇', '冬灵', '惜芹', '凌青', '谷芹', '雁桃', '映雁', '书兰', '盼香', '向山',
                   '寄风', '访烟', '绮晴', '映之', '醉波', '幻莲', '谷冬', '傲柔', '寄容', '以珊', '紫雪', '芷容', '书琴', '寻桃', '涵阳', '怀寒', '易云',
                   '代秋', '惜梦', '尔烟', '谷槐', '怀莲', '夜山', '芷卉', '向彤', '新巧', '语海', '灵珊', '凝丹', '小蕾', '迎夏', '慕卉', '飞珍', '冰夏',
                   '亦竹', '飞莲', '海白', '元蝶', '春蕾', '怀绿', '尔容', '小玉', '幼南', '凡梦', '碧菡', '初晴', '宛秋', '傲旋', '新之', '凡儿', '夏真',
                   '静枫', '痴柏', '恨蕊', '乐双', '念薇', '靖雁', '寄松', '丹蝶', '元瑶', '冰蝶', '念波', '迎松', '海瑶', '乐萱', '凌兰', '曼岚', '若枫',
                   '傲薇', '凡灵', '乐蕊', '秋灵', '谷槐', '觅云', '寻春', '恨山', '从寒', '忆香', '觅波', '静曼', '青寒', '笑天', '涵蕾', '元柏', '代萱',
                   '紫真', '千青', '雪珍', '寄琴', '绿蕊', '醉柳', '诗翠', '念瑶', '孤风', '曼彤', '怀曼', '香巧', '采蓝', '芷天', '尔曼', '巧蕊']


def get_random_name():
    status = random.random()
    if status <= 0.2:
        return random.choice(first_names) + random.choice(boy_last_names)
    elif status <= 0.4:
        return random.choice(first_names) + random.choice(girl_last_names)
    elif status <= 0.6:
        return random.choice(boy_last_names)
    else:
        return random.choice(girl_last_names)


def get_random_times(start, end, n, frmt="%Y-%m-%d"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    return [random.random() * (etime - stime) + stime for _ in range(n)]


class Employee(object):
    def __init__(self, id, name, gender, birthday, joindate, education, department, position):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.joindate = joindate
        self.education = education
        self.department = department
        self.position = position


class Education(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Department(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Position(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(object):

    def __init__(self):
        self.employees = []
        self.educations = []
        self.departments = []
        self.positions = []

    def add_education(self, education):
        self.educations.append(education)

    def add_department(self, department):
        self.departments.append(department)

    def add_position(self, position):
        self.positions.append(position)

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_education(self, id):
        for edu in self.educations:
            if edu.id == id:
                return edu

    def get_department(self, id):
        for dep in self.departments:
            if dep.id == id:
                return dep

    def get_position(self, id):
        for pos in self.positions:
            if pos.id == id:
                return pos

    def get_employee(self, id):
        for emp in self.employees:
            if emp.id == id:
                return emp

    def get_educations_by_name(self, name):
        return [edu for edu in self.educations if name in edu.name]

    def get_departments_by_name(self, name):
        return [dep for dep in self.departments if name in dep.name]

    def get_positions_by_name(self, name):
        return [pos for pos in self.positions if name in pos.name]

    def get_employees_by_name(self, name):
        return [emp for emp in self.employees if name in emp.name]

    def get_employees_by_gender(self, gender):
        return [emp for emp in self.employees if gender == emp.gender]

    def get_employees_by_education_id(self, education_id):
        return [emp for emp in self.employees if emp.education.id == education_id]

    def get_employees_by_department_id(self, department_id):
        return [emp for emp in self.employees if emp.department.id == department_id]

    def get_employees_by_position_id(self, position_id):
        return [emp for emp in self.employees if emp.position.id == position_id]

    def fill_test_data(self):
        self.educations = [
            Education(1, '小学'),
            Education(2, '初中'),
            Education(3, '高中'),
            Education(4, '本科'),
            Education(5, '硕士'),
            Education(6, '博士')
        ]
        self.departments = [
            Department(1, 'JAVA教研部'),
            Department(2, 'PYTHON教研部'),
            Department(3, 'UI教研部'),
            Department(4, 'LINUX教研部'),
            Department(5, 'PHP教研部'),
            Department(6, 'C++教研部')
        ]
        self.positions = [
            Position(1, '总监'),
            Position(2, '总监级讲师'),
            Position(3, '金牌讲师'),
            Position(4, '讲师'),
            Position(5, '助理讲师'),
            Position(6, '实训讲师'),
            Position(7, '助教'),
        ]

        for i in range(1, 101):
            self.employees.append(
                Employee(
                    i,
                    get_random_name(),
                    random.random() > 0.5,
                    get_random_times('1970-01-01', '2000-01-01', 1)[0],
                    get_random_times('2010-01-01', '2016-01-01', 1)[0],
                    random.choice(self.educations),
                    random.choice(self.departments),
                    random.choice(self.positions)
                )
            )


if __name__ == '__main__':
    manager = Manager()
    manager.fill_test_data()

    # 查找PYTHON教研部下所有的员工
    dep_python = manager.get_departments_by_name('PYTHON')[0]
    if dep_python:
        for emp in manager.get_employees_by_department_id(dep_python.id):
            print(emp.name, '男' if emp.gender else '女', emp.department.name, emp.position.name, emp.education.name)

    print('*' * 27)

    # 查找本科学历的所有员工
    edu_coll = manager.get_educations_by_name('本科')[0]
    if edu_coll:
        for emp in manager.get_employees_by_education_id(edu_coll.id):
            print(emp.name, '男' if emp.gender else '女', emp.department.name, emp.position.name, emp.education.name)
