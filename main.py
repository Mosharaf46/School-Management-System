from school import School
from person import Person,Student,Teacher
from subject import Subject
from classroom import ClassRoom

school=School('ABC','Dhaka')
#adding classroom
eight=ClassRoom('Eight')
nine=ClassRoom('Nine')
ten=ClassRoom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#adding student
rahim=Student('Rahim',eight)
karim=Student('Karim',nine)
fahim=Student("Fahim",ten)
hamim=Student("Hamin",ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

#adding teachers

abul=Teacher('Abul khan')
babul=Teacher('Babul khan')
bulbul=Teacher('Bulbul khan')
Hakim=Teacher('Hakim khan')
school.add_teacher('Bangla',abul)
school.add_teacher('Physics',babul)
school.add_teacher('chemistry',bulbul)
school.add_teacher('Biology',Hakim)
#adding subjects

bangla=Subject("Bangla",abul)
physics=Subject("physics",babul)
chemistry=Subject("chemistry",bulbul)
biology=Subject("Biology",bulbul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(biology)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()
print(school)