This project is intentionally simple,and purpose-driven. I avoided using a VectorDB because the problem didn’t require chunked document retrieval — all the behavioral logic was prompt-driven. Using vector search would have been over-engineering.

However, one area I’d explore further is caching. Caching previous user queries and responses could reduce API calls, save tokens, and improve speed — especially if a user revisits the bot or asks repeated questions. It would be a practical enhancement aligned with optimizing cost and latency in production-ready AI applications.
