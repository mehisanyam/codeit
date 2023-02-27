#include<stdio.h>

int reverse();        
int palindrome();
int factorial();
int arm();
int fibbo();
int prime();

int main(){            
    int num;
    printf(".........................................................................................\n");
    printf("1.Reverse\n2.Palindrome\n3.Factorial\n4.Armstrong number\n5.Fibbonacci number\n6.Prime numbers\n");
    printf(".........................................................................................\n");
    printf("Enter a number from the above list: ");
    scanf("%d",&num);
    switch(num){          
        case 1:
            reverse();
            break;
        case 2:
            palindrome();
            break;
        case 3:
            factorial();
            break;
        case 4:
            arm();
            break;
        case 5:
            fibbo();
            break;
        case 6:
            prime();
            break;
        default:
            printf("There is no such option available.");
            break;
    }
    return 0;
}

int reverse(){                  
    int temp=0,orignal,remainder,n;
    printf("Enter a number:");
    scanf("%d",&orignal);
    n=orignal;
    while (orignal>0)
    {
        remainder=orignal%10;
        temp=temp*10+remainder;
        orignal/=10;
    }
    printf("The reverse of %d is %d.",n,temp);
    return temp;
} 

int palindrome(){               
    int rev=0,orig,n,rem;
    printf("Enter a number: ");
    scanf("%d",&n);
    orig=n;
    while (n>0)
    {
        rem=n%10;
        rev=rev*10+rem;
        n/=10;

    }
    (rev==orig)?printf("%d is a palindrome.",orig):printf("%d is not a palindrome",orig);
    }

int factorial(){            
    int fact=1,n,i;
    printf("Enter a number: ");
    scanf("%d",&n);
    for ( i = 1;i<=n; i++)
    {
        fact=fact*i;
    }
    printf("Factorial of %d is %d.",n,fact);
}

int arm(){                  
    int r,sum=0,temp,n;
    printf("Enter a number:");
    scanf("%d",&n);
    temp=n;
    while (n>0)
    {
        r=n%10;
        sum=sum+(r*r*r);
        n/=10;
    }
    if (temp==sum)
    {
        printf("%d is an armstrong number.\n",temp);
    }
    else{
        printf("%d is a not an armstrong number.\n",temp);
    }
} 

int fibbo(){                
    int t1=0,t2=1,i,temp=0,n;
    printf("Enter a value: ");
    scanf("%d",&n);
    printf("%d\n%d\n",t1,t2);
    for ( i = 3;i<=n;++i)
    {
        temp=t1+t2;
        t1=t2;
        t2=temp;
        printf("%d\n",temp);
    }
}

int prime(){                
    int n,i,flag=1;
    printf("Enter a number: ");
    scanf("%d",&n);
    if (n==1||n==0)
    {
        flag=0;/* code */
    }
    for (i = 2; i <= n/2 ; ++i)
    {
        if (n%i==0){
            flag=0;
            break;
            /* code */
    }
    
    }
    if(flag==1){
        printf("%d is a prime number.",n);

    }
    else{
        printf("%d is not a prime number.",n);
    }
}
