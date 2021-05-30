courses=['History','Math','Physics','Chemistry']

for index,course in enumerate(courses,start=1):
    print(index,course)

course_str='-'.join(courses)
print(course_str)

new_list=course_str.split('--')
print(new_list)