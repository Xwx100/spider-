def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def clear_chinese(in_path,out_path):
    with open(in_path,'r',encoding='utf-8') as f:
        line = f.read()
        str = ''
        for word in line:
            if is_chinese(word):
               str += word
    with open(out_path,'w',encoding='utf-8') as s:
        s.write(str)

if __name__ == '__main__':
    clear_chinese('./fengyuchanglin.txt','./fengyu.txt')