// Keys mirror the LangGraph state keys in graph/state.py. The SSE
// handler assigns straight into this object with state[event.type],
// so a new agent output needs a key here plus matching entries in the
// STAGES and tabs lists in navigation.js.

window.state = {

    raw_resume: null,
    resume_analysis: null,
    job_analysis: null,
    gap_analysis: null,
    interview_analysis: null,
    learning_roadmap: null,
    market_analysis: null,
    cover_letter: null,

    activePage: "resume",

    loading: false,
    error: null

};
