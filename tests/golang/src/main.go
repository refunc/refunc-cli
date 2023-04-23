package main

import (
	"context"
	"fmt"
	"os"

	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
	Name string `json:"name"`
}

type MyResult struct {
	Code int    `json:"code"`
	Msg  string `json:"msg"`
}

func HandleRequest(ctx context.Context, event MyEvent) (*MyResult, error) {
	//return fmt.Sprintf("Hello %s!", name.Name), nil
	if event.Name != "Arvin" {
		return nil, fmt.Errorf("i don't konw you, %s", event.Name)
	}

	fmt.Println("loooooooooooooooooooog")

	return &MyResult{
		Code: 200,
		Msg:  fmt.Sprintf("Hello %s! Pid %d", event.Name, os.Getpid()),
	}, nil
}

func main() {
	lambda.Start(HandleRequest)
}
