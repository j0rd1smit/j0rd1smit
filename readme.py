from rich.console import Console
from rich.tree import Tree
def main():

    console = Console(record=True, width=100)

    tree = Tree("🙂 [link=https://jordismit.com/]Jordi Smit", guide_style="bold bright_black")

    online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
    online_tree.add("[bold link=https://jordismit.com/]jordismit.com[/] - [bright_black]personal blog")
    online_tree.add("[bold link=https://jordismit.com/tools/ai-based-transcription-in-the-browser/]Client side audio transcription in browser[/]")
    online_tree.add("[bold link=https://obsidian.md/plugins?search=Copilot%20auto%20completion/]Obsidian copilot auto completion[/] -[bright_black] Obsidian plugin")

    open_source_tree = tree.add("📦 Open Source", guide_style="bright_black")
    open_source_tree.add("[bold link=https://github.com/j0rd1smit/obsidian-copilot-auto-completion]Obsidian copilot auto completion[/] - [bright_black]Github repo")
    open_source_tree.add("[bold link=https://github.com/j0rd1smit/todoist_react_agent]ToDoist LLM Agent[/] - [bright_black]LLM agent that can manage your todoist-based todo lists")

    contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")
    contrib_tree.add("[bold link=https://github.com/getindata/kedro-azureml/pull/47]Kedro-AzureML[/] - [bright_black]Fix authorization issues on AzureML Compute Instance")
    contrib_tree.add("[bold link=https://github.com/Lightning-AI/lightning/pull/14368]PyTorch-lightning[/] - [bright_black]Fix memory corruption bug on M1 Macs")

    employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")

    xebia_tree = employer_tree.add("[bold link=https://xebia.com/digital-transformation/data-and-ai//]Xebia Data formaly known as GoDataDriven[/]  - [bright_black]Data and AI consultancy")
    xebia_tree.add("[bold link=https://github.com/godatadriven/Kedro-Azureml-Starter]Kedro-Azureml-Starter[/]  - [bright_black]A template and tutorial for AzureML-based Kedro projects")
    xebia_tree.add("[bold link=https://github.com/godatadriven/azureml_experiment_tracking_tutorial]AzureML-experiment-tracking-tutorial[/]  - [bright_black]Intro into experiment tracking on AzureML")

    talk_tree = tree.add("🎙️ Talks", guide_style="bright_black")
    talk_tree.add("[bold link=https://www.youtube.com/watch?v=jB5LGEjFVvU]Slack bots 101[/] - [bright_black]PyData Berlin 2022")
    talk_tree.add("[bold link=https://amsterdam2023.pydata.org/cfp/talk/N7Y7X7/]LLM Agents 101[/] - [bright_black]PyData Amsterdam 2023")

    blog_tree = tree.add("✏️️ Blogs", guide_style="bright_black")
    blog_tree.add("[bold link=https://jordismit.com/blog/what-does-it-take-to-add-copilot-to-obsidian/]What does it take to add Copilot to Obsidian?[/]")
    blog_tree.add("[bold link=https://jordismit.com/blog/what-does-it-take-to-let-chatgpt-manage-my-todoist-tasks/]What does it take to let ChatGPT manage my Todoist tasks?[/]")
    blog_tree.add("[bold link=https://jordismit.com/blog/the-surprising-impact-of-kedros-data-catalog/]The Surprising Impact of Kedro's' Data Catalog[/]")
    blog_tree.add("[bold link=https://jordismit.com/blog/adding-application-insight-based-monitoring-to-fast-api/]Adding Application Insight Based Monitoring to Fast API[/]")
    blog_tree.add("[bold link=https://jordismit.com/blog/diy-auto-grad-engine-a-step-by-step-guide-to-calculating-derivatives-automatically/]DIY auto-grad Engine[/]")
    blog_tree.add("[bold link=https://jordismit.com/blog/python-dataclass-from-scratch/]Python Dataclass From Scratch[/]")



    console.print(tree)
    console.print("")
    console.print("[green]Follow me on [bold link=https://www.linkedin.com/in/jordi-smit-8778b51b4]Linkedin[/]")

    CONSOLE_HTML_FORMAT = """<h1>Hi 👋, I'm Jordi Smit</h1>\n<p>A passionate Machine Learning Engineer from the Netherlands</p>\n<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>"""

    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)

if __name__ == '__main__':
    main()