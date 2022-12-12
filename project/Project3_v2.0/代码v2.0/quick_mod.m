%a^b mod k
function [ ans ] = quick_mod( a,b,k )

ans = 1;
a = mod(a,k);
while(b>0)
    if(mod(b,2)==1)
        ans = mod(ans*a,k);
    end
    b = b/2;
    b = fix(b);
    a = mod(a*a,k);
end

