\# 🚀 Demo Deployment Workflow (Vite + Vercel)



\*\*Goal:\*\* Add a new "Proof of Work" HTML demo to the portfolio and push it live.



\## Phase 1: Create the Demo

1\.  \*\*Generate the Project:\*\*

&nbsp;   \* Prompt the AI to create a "Standalone Vanilla HTML/JS tool."

&nbsp;   \* \*Note:\* Do not ask for React components for the demo itself. Keep it simple HTML so it runs in isolation.



2\.  \*\*Place the File:\*\*

&nbsp;   \* Navigate to the `public/` folder.

&nbsp;   \* (Optional) Create a subfolder like `public/demos/`.

&nbsp;   \* Create the new file: `public/demos/my-new-project.html`.

&nbsp;   \* Paste the HTML code there.



\## Phase 2: Link it in the Portfolio

1\.  \*\*Open the Menu File:\*\*

&nbsp;   \* Go to `src/App.jsx`.

&nbsp;   \* Locate the "Project Demo Stack" section (search for `fixed top-24`).



2\.  \*\*Add the Button:\*\*

&nbsp;   \* Copy the existing `<a href...>` line.

&nbsp;   \* Paste it directly below the previous one.

&nbsp;   \* \*\*Update the Link:\*\* Change `href="/demos/workday.html"` to `href="/demos/my-new-project.html"`.

&nbsp;   \* \*\*Update the Text:\*\* Change the label to the new project name.



\## Phase 3: Local Test (Safety Check)

1\.  \*\*Start Local Server:\*\*

&nbsp;   ```powershell

&nbsp;   npm run dev

&nbsp;   ```

2\.  \*\*Verify:\*\*

&nbsp;   \* Open the localhost link.

&nbsp;   \* Click the new button.

&nbsp;   \* Ensure the new HTML page loads correctly.

&nbsp;   \* \*Note:\* You do NOT need to run `npm run build` here.



\## Phase 4: Go Live (The Push)

Vercel will handle the building process. You just need to send the source code.



1\.  \*\*Stop the Server:\*\*

&nbsp;   \* Press `Ctrl + C` in the terminal to stop `npm run dev`.



2\.  \*\*Send to GitHub:\*\*

&nbsp;   ```powershell

&nbsp;   git add .

&nbsp;   git commit -m "Added \[Project Name] demo"

&nbsp;   git push

&nbsp;   ```



3\.  \*\*Wait \& Verify:\*\*

&nbsp;   \* Wait approx. 60 seconds.

&nbsp;   \* Go to your live URL: `https://pl-rez.vercel.app`

&nbsp;   \* Hard Refresh (`Ctrl + F5`) to see the new button.

