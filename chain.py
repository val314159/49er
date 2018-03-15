#!/usr/bin/env python
import os, sys, time, datetime, hashlib, shutil
class MineApp:
    V = ['0123456789abcdef','01234567','0123','01']
    def __init__(_):
        _.difficulty = 16
        _.ts = datetime.datetime.now()
        _.min_delta = datetime.timedelta(0,4)
        _.max_delta = datetime.timedelta(0,60)
        _.set_difficulty(-1)
        _.previous = 'PREV'
        _.blkno = 1
    def destroy_chain(_):
        print(">> destroy")
        try:   shutil.rmtree("c")
        except:  pass
    def create_chain(_):
        print(">> create")
        [os.mkdir(x) for x in ('c','c/n','c/t','c/p')]
        with open('c/n/genesis.yaml','w') as f:
            f.write("Let there be blocks!\n")
    def set_difficulty(_, adjustment):
        _.difficulty += adjustment
        q, r = divmod(_.difficulty, 4)
        _.pfx, _.off, _.ch = '0'*q, q, _.V[r]
    def read_blockno(_):
        line = open('c/o').readline().split()
        if line[0] == 'BlockNo:':
            _.blkno = int(line)
    def link_block(_):
        try:    _.read_blockno()
        except: pass
        _.blkno += 1
    def mk_hash(_, n, sig):
        h = hashlib.new('ripemd160')
        h.update(("%x\n%s" % (n, sig)).encode())
        return h.hexdigest()
    def _solve_block(_, sig, n = 0):
        while 1:
            n += 1
            hd = _.mk_hash(n, sig)
            if hd.startswith(_.pfx):
                if hd[_.off] in _.ch:
                    _.previous = "%s+%x" % (hd, n)
                    _.full_id = "$!FullId: " + _.previous
                    with open('c/p/f','w') as f:
                        f.write(_.full_id + '\n')
                    os.system('cat c/p/f c/d')
                    print('---')
                    return n, hd
    def sign_block(_):
        os.system("rm -f c/p/*")
        os.system("cp    c/d    c/o 2>/dev/null")
        os.system("cat   c/n/* >c/d 2>/dev/null ")
        os.system("openssl ripemd160 <c/d >c/p/sig")
        os.system("rm -f c/n/*")
    def solve_block(_):
        n, hd = _._solve_block(open("c/p/sig").read())
        os.system("echo %x >c/p/none" % n)
        os.system("cat c/p/*|openssl ripemd160 >c/id")
    def update_headers(_):
        _.prev_ts = _.ts
        _.ts = datetime.datetime.now()
        diff = _.ts - _.prev_ts
        if   diff < _.min_delta:  _.set_difficulty(+1)
        elif diff > _.max_delta:  _.set_difficulty(-1)
        with open('c/n/BlockNo','w') as f:
            f.write('BlockNo: %s\n' % _.blkno)
        with open('c/n/Date','w') as f:
            f.write('Date: %s\n' % _.ts.isoformat())
        with open('c/n/Difficulty','w') as f:
            f.write('Difficulty: %s\n' % _.difficulty)
        with open('c/n/Previous','w') as f:
            f.write('Previous: %s\n' % _.previous)
        with open('c/n/_','w') as f:
            f.write('\n')
        return
    def mine_block(_):
        _.sign_block()
        _.solve_block()
        _.update_headers()
        _.link_block()
        return
    def loop(_, reset = False):
        if reset: _.destroy_chain() ; _.create_chain()
        while 1:  _.mine_block()
def main(): MineApp().loop(reset=True)
if __name__ == '__main__': main()
