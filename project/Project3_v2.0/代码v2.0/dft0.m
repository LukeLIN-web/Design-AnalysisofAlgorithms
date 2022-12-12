function [ xk ] = dft0( xn )

 N=length(xn);
 WN=exp(-1i.*2.*pi./N);    
 xk=zeros(1,N);      
  n = 0:N-1;
 for k=0:N-1
   xk(k+1)=xn*WN.^(k.*n');  %此处下标一定得从1开始，因为matlab的下标是从1开始的

 end    
    
end
