function [ xk ] = dft0( xn )

 N=length(xn);
 WN=exp(-1i.*2.*pi./N);    
 xk=zeros(1,N);      
  n = 0:N-1;
 for k=0:N-1
   xk(k+1)=xn*WN.^(k.*n');  %�˴��±�һ���ô�1��ʼ����Ϊmatlab���±��Ǵ�1��ʼ��

 end    
    
end
