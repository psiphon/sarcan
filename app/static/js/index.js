'use strict';

const e = React.createElement;

class AudioMessage extends React.Component {
    constructor(props) {
        super(props);
        this.audioRef = React.createRef();
    }

    componentDidMount() {
        this.audioRef.current && this.audioRef.current.play();
    }

    render() {
        const textElement = e(
            'span',
            { className: 'text-message' },
            this.props.text
        );

        if (this.props.audio === null) {
            return textElement;
        }

        const audioElement = e(
            'audio',
            { 
                ref: this.audioRef, 
                src: this.props.audio, 
                hidden: true,                
                controls: false 
            }
        );

        return e(
            'div',
            {
                onClick: () => this.audioRef.current.play(),
                className: 'audio-message'                
            },
            textElement,
            audioElement
        );
    }
}

class UserMessage extends React.Component {
    render() {
        return e(
            'div',
            { className: 'user-message' },
            e(AudioMessage, { text: this.props.message, audio: null })
        );
    }
}

class BotMessage extends React.Component {
    render() {
        return e(
            'div',
            { className: 'bot-message' },
            e(AudioMessage, { text: this.props.message, audio: this.props.audio || null })
        );
    }
}

class SystemMessage extends React.Component {
    render() {
        return e(
            'div',
            { className: 'system-message' },
            e(AudioMessage, { text: this.props.message, audio: null })
        );
    }
}

class ChatHistory extends React.Component {
    constructor(props) {
        super(props);
        this.state = { chRef: React.createRef() };
    }


    render() {
        const messages = this.props.messages.map((message, index) => {
            if (message.user === 'user') {
                return e(UserMessage, { message: message.text, key: index });
            } else if (message.user === 'bot') {
                return e(BotMessage, { message: message.text, audio: message.audio, key: index });
            } else {
                return e(SystemMessage, { message: message.text, key: index });
            }
        });
        const chatHistoryElement =  e(
            'div',
            { className: 'chat-history' },
            [...messages, this.props.typing && e(TypingIndicator)]
        );

        // scroll to bottom
        if (this.state.chRef.current) {
            this.state.chRef.current.scrollTop = this.state.chRef.current.scrollHeight;
        }

        return e(
            'div',
            { 
                ref: this.state.chRef,
                className: 'chat-history-container' 
            },
            chatHistoryElement
        )
    }
}

class TypingIndicator extends React.Component {
    render() {
        return e(
            'div',
            { className: 'typing-indicator' },
            e('span', null, 'Typing...')
        );
    }
}

class ChatInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = { value: '' };
    }
    
    render() {
        const inputElement =  e(
            'input',
            {
                type: 'text',
                value: this.state.value,
                onKeyDown: (e) => {
                    if (e.key === 'Enter' || e.keyCode === 13) {
                        this.props.onSend && this.props.onSend(this.state.value);
                        this.setState({ value: '' });
                    }
                },
                onChange: (e) => this.setState({
                     value: e.target.value 
                }),
            }
        );
        const buttonElement = e(
            'button',
            {
                onClick: () => {
                    this.props.onSend && this.props.onSend(this.state.value);
                    this.setState({ value: '' });
                }
            },
            'Send'
        );
        return e(
            'div',
            { className: 'chat-input' },
            inputElement,
            buttonElement
        );
    }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
        messages: [],
        typing: false
    };
  }

  render() {
    const chatHistoryElement = e(ChatHistory, this.state);
    const chatInputElement = e(ChatInput, { onSend: (message) => {
        console.log(message);
        this.setState({ 
            ...this.state,
            typing: true,
            messages: this.state.messages.concat({
                user: 'user', 
                text: message, 
                audio: null
        })});
        
        fetch('/api/text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/text',
            },
            body: message,
        }).then(response => {
            console.info(response);
            if(response.status === 200) {
                response.json().then(data => {
                    console.log(data);
                    this.setState({ 
                        ...this.state,
                        messages: this.state.messages.concat({
                            user: 'bot',
                            text: data.message,
                            audio: data.audio
                        })
                    });
                });
            }else {
                console.log('Error:', response.status);
                this.setState({ 
                    ...this.state,
                    messages: this.state.messages.concat({
                        user: 'system',
                        text: 'Error: ' + response.status,
                        audio: null
                    })
                });
            }
        }).finally(() => {
            this.setState({ 
                ...this.state,
                typing: false
            });
        });
    }});

    return e(
      'div',
      { className: 'chat' },
      chatHistoryElement,
      chatInputElement
    );
  }
}

const domContainer = document.querySelector('body');
const root = ReactDOM.createRoot(domContainer);
root.render(e(App));