// See online documentation for examples
// https://docs.getdrafts.com/docs/actions/scripting
String.prototype.format = function () {
    if (arguments.length == 0) return this;
    var param = arguments[0];
    var s = this;
    if (typeof (param) == 'object') {
        for (var key in param)
            s = s.replace(new RegExp("\\{" + key + "\\}", "g"), param[key]);
        return s;
    } else {
        for (var i = 0; i < arguments.length; i++)
            s = s.replace(new RegExp("\\{" + i + "\\}", "g"), arguments[i]);
        return s;
    }
}
const addToc = content => {
    const headerLines = content.split('\n').filter(line => /^#+\s+[^\s]+/.test(line))
    if (headerLines.length == 0) {
        alert("No Markdown headers (e.g. ## Header) found")
        return
    }
    const tocLines = []
    let lastLevel = 0
    for (let i = 0; i < headerLines.length; i++) {
        const splitMatch = headerLines[i].match(/^(#+)\s+(.*)$/)
        // - 2 assumes the first header is h2
        const level = splitMatch[1].length - 2
        if (level < 0) {
            alert("h1 headers (#) are not compatible with Table of Contents. Please use h2 headers (##) and below.")
            return null
        }
        if (level > lastLevel + 1) {
            alert("Cannot make a table of contents if header levels are skipped, e.g. ## followed by ####")
            return
        }
        lastLevel = level
        const headerText = splitMatch[2]
        // tocLines.push("    ".repeat(level) + "* " + headerText + "test_toc")
        tocLines.push("{0}* [{1}](#{2})".format("    ".repeat(level), headerText, headerText))
    }
    if (tocLines[0][0] != "*") {
        alert("The first header must be a h2 (##)")
        return
    }

    let startMatch = content.match(/<!-- toc start -->/)
    let endMatch = content.match(/<!-- toc end -->/)
    if (startMatch == null && endMatch == null) {
        const firstHeaderMatch = content.match(/^(#+)\s+(.*)$/m)
        content = `${content.substring(0, firstHeaderMatch.index)}<!-- toc start --><!-- toc end -->\n\n${content.substring(firstHeaderMatch.index)}`
        startMatch = content.match(/<!-- toc start -->/)
        endMatch = content.match(/<!-- toc end -->/)
    }
    if (startMatch == null || endMatch == null) {
        alert("You need both <!-- toc start --> and <!-- toc end --> in your draft to place a table of contents")
        return
    }
    if (endMatch.index < startMatch.index) {
        alert("<!-- toc start --> must come before <!-- toc end -->")
        return
    }
    const startPos = startMatch.index + startMatch[0].length
    const endPos = endMatch.index
    return `${content.substring(0, startPos)}\n${tocLines.join("\n")}\n${content.substring(endPos)}`
}

const newBody = addToc(draft.lines.slice(1).join("\n"))
if (newBody != null) {
    draft.content = `${draft.lines[0]}\n${newBody}`
    draft.update()
}