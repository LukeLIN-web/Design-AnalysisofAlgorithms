function [ g,order, inv_order, Hs ] = my_rader( hs )
%implment Rader's algorithm

p = length(hs);
h0 = hs(1);

%补0至长度为m
temp = 0;
while (power(2,temp)<2*p-3)
    temp=temp+1;
end
m=power(2,temp);

%get generator of p
g=0;
for i=2:p-1
    unique_seq=zeros(1,p-1);
    found_g=1;
    trace=1;
    for j=0:p-2
        %temp=mod(power(i,j),p);
        temp=quick_mod(i,j,p);
        if ismember(temp,unique_seq)
            found_g=0;
            break;
        end
        unique_seq(trace)=temp;
        trace=trace+1;
    end
    if (found_g==1)
        g = i;
        break;
    end
        
end

order=zeros(1,p-1);
reorder_hs=zeros(1,p-1);
for i=0:1:p-2
    %order(i+1)=mod(power(g,i),p);
    order(i+1)=quick_mod(g,i,p);
    reorder_hs(i+1) = hs(order(i+1)+1);
end


%求数论逆元，可以用快速幂运算优化或者用扩展欧几里得算法求逆元
inv_order=zeros(1,p-1);
for i=1:p-1
    inv_order(i)=quick_mod(order(i),p-2,p);
end

ws=zeros(1,p-1);
for i=1:p-1
    ws(i)=exp(-2*pi*1i*inv_order(i)/p);% 1i第一个字符是数字1,1i表示复数里的i
end

e_ro_hs=zeros(1,m);
e_ro_hs(1)=reorder_hs(1);
for i=3+m-p:m
    e_ro_hs(i)=reorder_hs(i-(1+m-p));
end

e_ws=zeros(1,m);
for i=1:p-1
   e_ws(i)=ws(i);
end
for i=p:m
    temp=mod(i,p-1);
    if (temp==0)
        temp=p-1;
    end
    e_ws(i)=ws(temp);
end

hs_dft=fft(e_ro_hs);
ws_dft=fft(e_ws);
Hs=zeros(1,p);
Hs(1)=sum(hs);

temp_Hs=hs_dft.*ws_dft;
temp_Hs=ifft(temp_Hs);
temp_Hs=temp_Hs+h0;

for i=1:p-1
    Hs(inv_order(i)+1)=temp_Hs(i);
end

end

