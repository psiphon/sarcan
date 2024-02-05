# Sarcastic Artificially Rationalized Companion And Naysayer (SARCAN) - The Sarcastic AI Assistant

## Overview:
SARCAN is an advanced AI assistant designed to inject sarcasm and humor into your interactions, offering users the flexibility to choose between receiving responses in WAV format or text. Whether you prefer typing out your queries or submitting voice input through WAV files, SARCAN caters to your preferences by delivering responses in your chosen format. Powered by ChatGPT as its brain and seamlessly integrated with the Google Assistant SDK, SARCAN combines advanced natural language processing with a keen sense of humor to provide personalized and entertaining responses.

## Key Features:
1. Sarcasm Integration: SARCAN is programmed to understand and respond with sarcasm, adding wit and humor to conversations and interactions.
2. Multi-Modal Input and Output: SARCAN accepts both text input and voice input (via WAV files) and allows users to specify whether they want responses in WAV format or text, ensuring a seamless and customizable experience.
3. ChatGPT Brain: SARCAN leverages ChatGPT's language models to generate contextually relevant and witty responses tailored to the user's input.
4. Google Assistant SDK Integration: SARCAN seamlessly integrates with the Google Assistant SDK, enabling users to control smart devices and access services through voice commands.
5. Personalization: SARCAN learns from user interactions to tailor its responses and humor to individual preferences, creating a more engaging and personalized experience over time.
6. Multi-Platform Support: SARCAN is accessible across various platforms, including mobile devices, smart speakers, and web browsers, ensuring users can interact with the assistant wherever they are.

## Benefits:
1. Enhanced User Experience: With the option to specify response format, SARCAN provides a customizable and interactive user experience, catering to individual preferences.
2. Entertainment: SARCAN adds humor and entertainment to everyday interactions, making tasks more enjoyable and memorable.
3. Increased Productivity: Despite its playful nature, SARCAN remains capable of performing useful tasks and providing helpful information, enhancing productivity while keeping users entertained.
4. Technological Integration: By seamlessly integrating with the Google Assistant SDK and offering response format customization, SARCAN offers users greater flexibility and control over their digital experiences.

In summary, SARCAN stands out as an AI assistant that not only entertains with its sarcastic personality but also provides a customizable and engaging experience, allowing users to specify their preferred response format.

## Getting Started

Follow these steps to set up SARCAN on your system:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/<sarcan_repository_url>.git
    ```

2. **Setup Configuration**
    Create a `config.json` file inside the `config` directory. You can use the provided `config.json.example` as a template. Customize the configuration according to your preferences and requirements.

3. **Create Temporary Folder**
    Create a `tmp` folder in the SARCAN directory. This folder will be used for storing temporary files generated during the TTS synthesis process.

4. **Install Dependencies**
    Install espeak on your system using your package manager such as brew,yum,apt

    Install the required Python dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run SARCAN**
    You're all set! Run SARCAN using the provided scripts or integrate it into your own projects as needed.

#### Configuration Options

The `config.json` file allows you to customize various aspects of SARCAN's behavior, including input text preprocessing, voice selection, and output settings. Refer to the comments in the `config.json.example` file for details on each configuration option.

#### Usage

Once SARCAN is set up and configured, you can use it to generate speech from text programmatically or via the command line interface. Explore the provided scripts and documentation to understand how to integrate SARCAN into your workflow.

#### Contributions

Contributions to SARCAN are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

#### License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.

#### Acknowledgments

SARCAN relies on various open-source libraries and resources. We would like to thank the contributors of these projects for their valuable work.

Happy TTS synthesis with SARCAN! 🎙️🔊