async function startStreaming(formData, callbacks) {

    try {

        const response = await fetch("/analyze-stream", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {

            callbacks.onError?.("Server request failed.");

            return;

        }

        if (!response.body) {

            callbacks.onError?.("Streaming not supported.");

            return;

        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        let buffer = "";

        while (true) {

            const { value, done } = await reader.read();

            if (done) {

                callbacks.onComplete?.();

                break;

            }

            buffer += decoder.decode(value, { stream: true });

            const chunks = buffer.split("\n\n");

            buffer = chunks.pop();

            for (const chunk of chunks) {

                if (!chunk.startsWith("data: "))
                    continue;

                try {

                    const event = JSON.parse(
                        chunk.replace("data: ", "")
                    );

                    if (event.error) {

                        callbacks.onError?.(event.error);

                        return;

                    }

                    callbacks.onEvent?.(event);

                }
                catch (err) {

                    console.error("Invalid SSE event:", err);

                }

            }

        }

    }
    catch (err) {

        console.error(err);

        callbacks.onError?.("Unable to connect to the server.");

    }

}