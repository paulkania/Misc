package main

import "fmt"

func main() {

	trex := 15
	fmt.Println(trex) //15
	fmt.Println(&trex) //hexaddress
	fmt.Println() //hexaddress
	//fmt.Println(*trex) //error, will need to commeneted out

	zelox := &trex
	fmt.Println(zelox) //
	fmt.Println(&zelox) //
	fmt.Println(*zelox) //
	fmt.Println() //

	ccc := &zelox
	fmt.Println(ccc) //
	fmt.Println(&ccc) //
	fmt.Println(*&**ccc) //
	fmt.Println(*&*&**ccc) //
	fmt.Println() //


}
