class Student():

    def __init__(self, name, conf):
        self.name = name
        self.exam_max = conf['exam_max']
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.k = conf['k']
        self.marks = [0 for i in range(conf['lab_num'])]
        self.attempt_max = 3
        self.labs_attempts = [0 for i in range(conf['lab_num'])]
        self.exam_attempt = 0
        self.exam_mark = 0


    def make_lab(self, mark, lab=-1):
        if mark > self.lab_max:
            mark = self.lab_max
        if 0 <= lab < self.lab_num and self.labs_attempts[lab] < self.attempt_max:
            self.marks[lab] = mark
            self.labs_attempts[lab] += 1
        elif lab == -1:
            i = self.marks.index(0)
            if self.labs_attempts[i] <= self.attempt_max:
                self.marks[i] = mark
                self.labs_attempts[i] += 1
        return self

    def make_exam(self, mark):
        if mark > self.exam_max:
            mark = self.exam_max
        if self.exam_attempt <= self.attempt_max:
            self.exam_attempt += 1
            self.exam_mark = mark
        return self

    def is_certified(self):
        sum_marks = 0
        for point in self.marks:
            sum_marks += point
        sum_marks += self.exam_mark
        if sum_marks >= (self.exam_max + (self.lab_num * self.lab_max))*self.k:
            return sum_marks, True
        return sum_marks, False

    def __str__(self):
        return 'Student -- {} \n' \
               'Mark for exam = {} \n' \
               'Marks for labs = {} \n' \
            .format(self.name, self.exam_mark, self.marks)


if __name__ == '__main__':
    Misha = Student('Mikhail Mikhailovich', {'exam_max': 30, 'lab_max': 7, 'lab_num': 3, 'k': 0.61})
    Misha.make_lab(7, 0)
    Misha.make_lab(5, 1)
    Misha.make_lab(2, 2)
    Misha.make_exam(30)
    print(Misha)
    print(Misha.is_certified())

