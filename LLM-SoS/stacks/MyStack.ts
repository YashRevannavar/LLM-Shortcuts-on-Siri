import {StackContext, Function, Api, Config} from "sst/constructs";

const CUSTOM_TIMEOUT = 15 * 60;  // 15 minutes
export function MyStack({stack}: StackContext) {
    // 0) Create a secret const
    const MISTRAL_API_KEY = new Config.Secret(stack, "MISTRAL_API_KEY");
    const NEWS_URL = new Config.Secret(stack, "NEWS_URL");

    // 1) Create a basic Python Lambda
    const llm_daily_response = new Function(stack, "LlmDailyResponse", {
        runtime: "python3.11",
        handler: "packages/functions/src/llm_daily_response/app.handler",
        timeout: CUSTOM_TIMEOUT,
        architecture: "arm_64",
        bind: [MISTRAL_API_KEY, NEWS_URL]
    });
    // 2) Create an API Gateway
    const api = new Api(stack, "MyApi", {
        routes: {
            "GET /daily": {
                function: llm_daily_response,
            },
        },
    });
    // 3) Add outputs
    stack.addOutputs({
        LlmDailyResponse: llm_daily_response.functionName,
        ApiEndpoint: api.url,
    });
}