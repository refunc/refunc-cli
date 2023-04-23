package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/aws/aws-lambda-go/lambda"
)

type Payload struct {
	Body string `json:"body"`
}

type MyEvent struct {
	Name string `json:"name"`
}

type MyResult struct {
	Code int    `json:"code"`
	Msg  string `json:"msg"`
}

func HandleRequest(ctx context.Context, pay Payload) (*MyResult, error) {
	//return fmt.Sprintf("Hello %s!", name.Name), nil
	var event MyEvent
	err := json.Unmarshal([]byte(pay.Body), &event)
	if err != nil {
		return nil, err
	}
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
