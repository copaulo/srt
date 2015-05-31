class Srt:
    _srt = {}
    def __init__(self,path):
        self.data = open(path,'r').read().splitlines()
        self._parse()
    def _parse(self):
        line = 1
        x = 0
        while x < len(self.data):
            if str(line) != self.data[x]:
                raise ValueError('Error parsing srt file.')
            f = {'time':self.data[x+1],'text':''}
            x+=2
            text = []
            while self.data[x]!='':
                text.append(self.data[x])
                x+=1
            text = '\n'.join(text)
            f['text'] = text
            self._srt[line] = f
            x+=1
            line+=1
            
    def get_text(self,line):
        return self._srt[line]['text']
    
    def get_time(self,line):
        return self._srt[line]['time']
    
    def get_stime(self,line):
        def _convert(time):
            a,b,c = time.split(':')
            c,d = c.split(',')
            a = int(a)*60**2
            b = int(b)*60
            c = int(c)
            d = round(float('0.{}'.format(d)),3)
            return a+b+c+d
        begin,end = self._srt[line]['time'].split(' --> ')
        return (_convert(begin),_convert(end))
    
    def replace_text(self,line,newtext):
        self._srt[line]['text'] = newtext
    def save(self,path):
        file = open(path,'w')
        srt = ''
        for line in range(1,max(list(self._srt.keys()))+1):
            tr = str(line)+'\n'+self._srt[line]['time']+'\n'
            for i in self._srt[line]['text'].split('\n'):
                tr += i+'\n'
            tr += '\n'
            srt += tr
        file.write(srt)
        file.close()
 
