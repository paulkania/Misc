package main
import "fmt"

func GenericFinder(valuetofind float64,aslice []float64) bool{
	for _,value := range aslice {
		if valuetofind == value{
			return true
		}
	}
	return false
}

func main(){
myslice := []float64{3.21,1,4,5.66,99.45344,3.141529}
myslice[1] = 69.96
fmt.Println(myslice)
fmt.Println(GenericFinder(3,myslice))
}
