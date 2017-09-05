import java.util.*;

/*
    python의 퍼포먼스가 너무 떨어져서 java로 다시 구현
*/

class prob10 {
    private static List<Integer> primes = new ArrayList<>();

    public static void main(String[] args) {
        int limit = 2000000;
        long sum = 0;
        for(int i = 2; i <= limit; i++) {
            if(prob10.isPrime(i)) {
                prob10.primes.add(i);
                sum += (long)i;
            }
        }
        System.out.println(sum);
    }

    private static boolean isPrime(int num) {
        if(num == 2) {
            return true;
        } else {
            for(int i = 0; i < prob10.primes.size(); i++) {
                if(num % prob10.primes.get(i) == 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
