#! coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    print 'hello'
    print "中文"


    f = open("rdata")
    info=[]
    for line in f:
        info.append(line)
        print line
    f.close()
    index=1
    info.reverse()
    print info
    rate= 0
    to_price=0
    ret_list=[]
    for line in info:
        (d1,d2,d3,d4,turnover) = line.split()
        #print d1,d2,d3,d4,turnover
        to_price += (float(d1)+float(d2)+float(d3)+float(d4))/4*float(turnover)/100
        #print to_price
        rate += float(turnover)
        if rate > 100:
            ret = to_price/rate*100
            ret_list.append(ret)
            to_price=0
            rate=0




    ret_list.reverse() 
    for i in ret_list:
        print i
