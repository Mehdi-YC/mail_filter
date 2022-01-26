package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("Hello world!")
	for _, x := range []int{1, 2, 3} {
		fmt.Println(x)
	}
	a := func() (elts []string) {
		for _, ele := range []string{"dz", "algerie"} {
			if strings.Contains("mehdidouy@gmail.com", ele) {
				elts = append(elts, ele)
			}
		}
		return
	}()

	
    if len(a) > 0 {fmt.Println(true)
	} else {fmt.Println(false)}



}

