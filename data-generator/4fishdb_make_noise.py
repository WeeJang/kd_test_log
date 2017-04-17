#/usr/bin/env python2

import hashlib
import time

RESERVE_PRFIX = "0e75daa74cd0218"

time_counter = 0
def get_md5(raw):
	global time_counter
	raw += time_counter
	time_counter += 1
	md5 = hashlib.md5()
	md5.update(str(raw))
	return md5.hexdigest()[8:24]


def get_random_val():
	global RESERVE_PRFIX
	time_str = time.time()
	hash_time_str = get_md5(time_str)
	while hash_time_str.startswith(RESERVE_PRFIX):
		time_str = time.time()
		hash_time_str = get_md5(time_str)
	return hash_time_str		


tri_1_format = "%s\tstudent.type\tmaster"
tri_2_format = "%s\tperson.name\t%s"
tri_3_format = "%s\tstudy.follow\t%s"

tri_1_amount = 130
tri_2_amount = 200
tri_3_amount = 130


for i in xrange(tri_1_amount):
	tri_1_str = get_random_val()
	print tri_1_format % (tri_1_str,)
	stu_i = "stu_%s" % (i,)
	print tri_2_format % (tri_1_str,stu_i)
	for j in xrange(tri_2_amount):
		doc_j = "Doc_%s_%s" % (i,j,)
		tri_2_str = get_random_val()
		print tri_2_format % (tri_2_str,doc_j)
		print tri_3_format % (tri_1_str,tri_2_str)
		for m in xrange(tri_3_amount):
			doc_m = "DDoc_%s_%s_%s" % (i,j,m,)
			tri_3_str = get_random_val()
			print tri_2_format % (tri_3_str,doc_m)
			print tri_3_format % (tri_2_str,tri_3_str)
