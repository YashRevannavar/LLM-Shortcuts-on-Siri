import {StackContext, Function, Api} from "sst/constructs";

const CUSTOM_TIMEOUT = 15 * 60; // 15 minutes

export function MyStack({stack}: StackContext) {
    // 1) Create a basic Python Lambda
    const llm_daily_response = new Function(stack, "LlmDailyFunction", {
        runtime: "python3.11",
        handler: "packages/functions/src/llm_daily_response/app.handler",
        timeout: CUSTOM_TIMEOUT,
        architecture: "arm_64",
        permissions: ["bedrock:InvokeModel"],
    });

    const api = new Api(stack, "MyApi", {
        routes: {
            "GET /daily": {
                function: llm_daily_response,
            },
        },
    });

    stack.addOutputs({
        LlmDailyFunctionName: llm_daily_response.functionName,
        ApiEndpoint: api.url,
    });
}
