#include<iostream>
#include<bits/stdc++.h> 
#define MOD 1000000007
using namespace std;
void gen(vector <long long int> lists,long long int l,long long int r){
	long long int val,sums=0,score,diff=r-l,round;
	if(l%60==0){
		round=diff/60;
		score=round*(280);
		for(int i=1;i<=(r%60);i++){
			sums+=lists[i];
		}
		val=sums+score;
		cout<<val%MOD<<endl;
	}
	else if(diff>=59){
		val=l%60;
		diff=r-l;
		for(int i=val;i<=59;i++){
			sums+=lists[i];
		}
		
		l=l-(l%60)+60;
		round=(r-l)/60;
		if(round>=0){
		score=round*280;
		}
		for(int j=1;j<=(r%60);j++){
			sums+=lists[j];
		}
		val=score+sums;
		cout<<val%MOD<<endl;
	}
	else{
		if((r%60)>=59){
			for(int j=l%60;j<=59;j++){
				sums+=lists[j];
			}
			r=r-59;
			for(int i=1;i<=r%60;i++){
				sums+=lists[i];
			}
		cout<<sums%MOD<<endl;
	}
	else{
		for(int i=(l%60);i<=(r%60);i++){
			sums+=lists[i];
		}
		cout<<sums%MOD<<endl;
		
	}
	}
}

void fib(vector <long long int> lists,long long int l,long long int r){
	lists[0]=0;
	lists[1]=1;
	for(int i=2;i<=60;i++){
		lists[i]=(lists[i-1]+lists[i-2])%10;
	}
	gen(lists,l,r);	
}
int main(){
	int tc;
	cin>>tc;
	while(tc--){
	long long int l,r;
	std::cin>>l>>r;
	vector <long long int> lists(62);
	fib(lists,l,r);
}
}
