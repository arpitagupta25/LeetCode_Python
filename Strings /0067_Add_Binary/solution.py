class Solution(object):
    def addBinary(self, a, b):
        carry='0'
        i=len(a)-1
        j=len(b)-1
        final_ans=''
        result_dict={('0','0','0'):'00',('1','0','0'):'01',('0','0','1'):'01',('1','0','1'):'10',('0','1','0'):'01',('1','1','0'):'10',('0','1','1'):'10',('1','1','1'):'11'}
        while i>-1 and j>-1:
            ans_sum=result_dict[carry,a[i],b[j]]
            carry=ans_sum[0]
            final_ans=ans_sum[1]+final_ans
            i-=1
            j-=1
        while i>-1 or j>-1:
            if i>-1:
                ans_sum=result_dict[carry,a[i],'0']
                i-=1
            else:
                ans_sum=result_dict[carry,'0',b[j]]
                j-=1
            carry=ans_sum[0]
            final_ans=ans_sum[1]+final_ans
        if carry=='1':
            final_ans=carry+final_ans
        return final_ans
        

               
