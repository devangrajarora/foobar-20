// gearing-up-for-destruction

class GearingUpForDestruction {

	    public static int[] solution(int[] pegs) {
	        
	        int num = -pegs[0], n = pegs.length, denom;

	        if(n%2==0){
	        	num += pegs[n-1];
	        	denom = 3;
	        } else {
	        	num -= pegs[n-1];
	        	denom = 1;
	        }

	        for(int i = 1 ; i < n - 1 ; i++) {
	            if(i%2==1) num += (2*pegs[i]);
	            else num -= (2*pegs[i]);
	        }

	        num *= 2;

	        if(num%denom==0) {
	        	num = num/denom;
	        	denom = 1;
	        }

	        if(num/denom < 1) return new int[] {-1,-1};
	        
	        float radius = (float)num/(float)denom;

	        for(int i = 0 ; i < n - 1 ; i++) {

	        	int r1plusR2 = pegs[i+1] - pegs[i];
	        	if(radius >= r1plusR2 || radius < 0) return new int[]{-1,-1};
	        	radius = r1plusR2 - radius;
	        }

	        return new int[]{num,denom};
    }

	public static void main(String[] args) {
		
		int a[] = new int[]{4, 30, 50};
		a = solution(a);
		for(int i = 0 ; i < a.length ; i++) {
			System.out.print(a[i] + " ");
		}

		System.out.println();
	}

}