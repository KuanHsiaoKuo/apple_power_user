/**
 * @jest-environment jsdom
 */
import "@testing-library/jest-dom";
import { render, screen, waitFor } from "@testing-library/react";
import user from "@testing-library/user-event";
import React from "react";

import { QuestionView } from "../lib/questions/mod";
import { ShortAnswer } from "../lib/questions/short-answer";
import { submitButton } from "./utils";

describe("ShortAnswer", () => {
  let question: ShortAnswer = {
    type: "ShortAnswer",
    prompt: { prompt: "Hello world" },
    answer: { answer: "Yes" },
  };

  let submitted: any | null = null;
  beforeEach(async () => {
    submitted = null;
    render(
      <QuestionView
        question={question}
        index={1}
        onSubmit={answer => {
          submitted = answer;
        }}
      />
    );
    await waitFor(() => screen.getByText("Hello world"));
  });

  it("initially renders", () => {});

  it("validates input", async () => {
    await user.click(submitButton());
    expect(submitted).toBe(null);
  });

  it("accepts valid input", async () => {
    let input = screen.getByRole("textbox");
    await user.type(input, "foobar");
    await user.click(submitButton());
    expect(submitted).toStrictEqual({
      answer: { answer: "foobar" },
      correct: false,
    });
  });
});
