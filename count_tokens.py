import argparse
import tiktoken

# Input token prices per 1M tokens (USD)
MODEL_PRICES = {
    "gpt-4o-mini": 0.15,
    "gpt-4o": 2.50,
    "gpt-4.1": 2.00,
    "gpt-4.1-mini": 0.40,
}

parser = argparse.ArgumentParser(
    description="Calculate token count and estimated input cost."
)

parser.add_argument("filename", help="Text file to analyze")
parser.add_argument("model", help="OpenAI model name")

args = parser.parse_args()

enc = tiktoken.encoding_for_model(args.model)

with open(args.filename, "r", encoding="utf-8") as f:
    text = f.read()

tokens = enc.encode(text)
token_count = len(tokens)

print("Token count:", token_count)

if args.model in MODEL_PRICES:
    cost_per_million = MODEL_PRICES[args.model]
    cost = (token_count / 1000000) * cost_per_million

    print(f"Model: {args.model}")
    print(f"Input price: ${cost_per_million}/1M tokens")
    print(f"Estimated cost: ${cost:.8f}")
else:
    print(f"Pricing not available for model '{args.model}'")