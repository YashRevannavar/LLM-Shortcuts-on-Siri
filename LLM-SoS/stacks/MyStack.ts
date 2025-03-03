import { StackContext, Function, Api } from "sst/constructs";

export function MyStack({ stack }: StackContext) {
  // 1) Create a basic Python Lambda
  const llm_daily_response = new Function(stack, "MyPythonLambda", {
    runtime: "python3.11",
    handler: "packages/functions/src/llm_daily_response/main.handler",
  });

  const api = new Api(stack, "MyApi", {
    routes: {
      "GET /daily": {
        function: llm_daily_response,
      },
    },
  });

  stack.addOutputs({
    MyPythonLambdaName: llm_daily_response.functionName,
    ApiEndpoint: api.url,
  });
}