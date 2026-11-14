# VisionQC Design System

**File:** `design.md`  
**Version:** 1.0  
**Project:** VisionQC  
**Design reference:** [Outtake](https://www.outtake.ai/)  
**Status:** Approved visual direction

---

# 1. Design Philosophy

## 1.1 The visual identity

VisionQC should communicate:

- Precision
- Reliability
- Technical competence
- Industrial quality
- Clarity
- Control

The interface should look like software used by an actual manufacturing quality team.

It should not look like a generic AI-generated SaaS dashboard.

### Core design direction

**Industrial precision meets contemporary SaaS.**

The visual language combines:

1. Strong editorial typography.
2. Restrained blue-grey colours.
3. Clear geometric layouts.
4. Thin borders and structured surfaces.
5. Compact technical metadata.
6. Real product screenshots and inspection imagery.
7. Subtle, functional interactions.

The interface should be visually distinctive without relying on decorative effects.

## 1.2 Design principles

| Principle | Implementation |
|---|---|
| Precision | Consistent spacing, alignment and typography |
| Restraint | Limited colour palette and minimal decoration |
| Clarity | Clear hierarchy and descriptive labels |
| Authenticity | Real model results and actual product imagery |
| Functionality | Every visual element serves a purpose |
| Consistency | Shared components across every page |
| Trust | Accurate data, transparent model information and clear system states |

---

# 2. Reference Website Analysis

The Outtake website provides a useful design direction through the following characteristics.

## 2.1 Colour

Its visual direction uses a blue and grey palette, supported by strong dark and light contrast.

**What VisionQC should adopt:**

- Neutral backgrounds.
- Dark, high-contrast typography.
- Restrained blue accents.
- Grey supporting surfaces.
- Colour used to communicate status and interaction.

**What VisionQC should avoid:**

- Purple gradients.
- Rainbow gradients.
- Excessive neon colours.
- Random coloured cards.
- Decorative gradients behind headings.

## 2.2 Layout

The reference uses distinct content sections with clear visual hierarchy.

Notable characteristics:

- Strong section introductions.
- Large, confident headings.
- Structured content blocks.
- Visual product demonstrations.
- Alternating content arrangements.
- Clear separation between sections.
- Generous whitespace.

**VisionQC adaptation:**

Use a structured application shell with a fixed-width sidebar, a clear top navigation area and a controlled content grid.

The dashboard should prioritize actual inspection results and system information instead of decorative marketing cards.

## 2.3 Typography

The reference is identified with:

- Roobert: Primary sans-serif typeface.
- Geist Mono: Technical and monospace typeface.

These are suitable references for VisionQC.

The recommended approach is to use a confident sans-serif for headings and interface text, with a monospace family for technical information.

## 2.4 Component style

The design direction favours:

- Clean navigation.
- Strong text hierarchy.
- Restrained borders.
- Clearly differentiated sections.
- Purposeful visual elements.
- Product-oriented content.

For VisionQC, translate this into:

- Rectangular buttons.
- Structured tables.
- Subtle card surfaces.
- Thin separators.
- Clear status indicators.
- Functional charts.
- Image inspection panels.

## 2.5 Motion

Motion should be intentional.

Use small transitions to communicate changes in state, reveal content and improve navigation.

Do not use excessive scroll-triggered animations, animated backgrounds or cursor effects.

---

# 3. Colour System

The following colours are proposed for VisionQC. They are an original adaptation of the reference's restrained blue-grey direction, not claimed to be Outtake's exact colour values.

## 3.1 Primary palette

| Token | Hex | Usage |
|---|---|---|
| Ink | `#111820` | Primary text and dark surfaces |
| Graphite | `#202A35` | Secondary dark surfaces |
| Steel Blue | `#476985` | Primary brand accent |
| Muted Blue | `#7892A8` | Secondary accent |
| Paper | `#F5F6F5` | Main application background |
| White | `#FFFFFF` | Cards and elevated surfaces |
| Border | `#DCE1E4` | Borders and separators |
| Muted Grey | `#687580` | Supporting text |
| Light Grey | `#EBEEF0` | Secondary backgrounds |

## 3.2 Semantic colours

Semantic colours must communicate actual application states.

| State | Colour | Hex |
|---|---|---|
| OK / Approved | Muted green | `#34765B` |
| Defective / Critical | Restrained red | `#B64B46` |
| Warning | Industrial amber | `#B27A32` |
| Informational | Steel blue | `#476985` |
| Inactive | Grey | `#7C8790` |

Do not use these colours as decorative accents.

For example:

- Green means a successful or approved state.
- Red means a defective classification, critical error or failed state.
- Amber means a warning or pending attention.
- Blue means neutral information or an active interface element.

Never communicate status through colour alone. Include a text label or another recognizable indicator.

## 3.3 Colour distribution

Use the following approximate distribution:

- 65% neutral backgrounds.
- 25% text, borders and structural surfaces.
- 10% accent and semantic colours.

The exact distribution can vary by page, but accent colours must remain restrained.

## 3.4 Dark surfaces

Dark surfaces should be used selectively.

Recommended uses:

- Sidebar.
- Technical inspection workspace.
- Model information panels.
- Selected visualization areas.

Do not make every page dark. The default application should use a light, neutral canvas with strong contrast.

---

# 4. Typography System

## 4.1 Recommended font families

| Role | Typeface | Usage |
|---|---|---|
| Display | Roobert | Major headings and section titles |
| Interface | Roobert | Navigation, buttons and body text |
| Technical | Geist Mono | IDs, timestamps, model versions and metrics |

Roobert is a commercial typeface. Confirm licensing before using it in the project.

If a licensed copy is unavailable, use Geist Sans as the primary alternative.

Do not download or redistribute commercial font files without the appropriate licence.

## 4.2 Typography scale

| Element | Desktop size | Weight |
|---|---:|---:|
| Hero heading | 52-64px | 600 |
| Page heading | 36-44px | 600 |
| Section heading | 26-32px | 600 |
| Card heading | 18-21px | 550 |
| Body text | 14-16px | 400 |
| Supporting text | 12-13px | 400 |
| Technical metadata | 11-13px | 450 |
| Navigation | 13-14px | 500 |

Use sentence case for most interface labels.

Uppercase text should be reserved for small technical labels, section identifiers and metadata.

## 4.3 Typography rules

- Use a clear hierarchy.
- Avoid excessively large headings inside application screens.
- Keep body text readable.
- Use monospace only where it improves technical readability.
- Use tabular numerals for measurements and metrics.
- Avoid excessive font weights.
- Avoid unnecessary italic text.
- Do not use more than two primary font families.

---

# 5. Layout System

## 5.1 Application shell

VisionQC is primarily an operational dashboard.

The main application layout should use:

- Left navigation sidebar.
- Top application header.
- Main content region.
- Contextual action area.
- Consistent content width.
- Responsive behavior.

### Desktop layout

```text
+--------------------------------------------------------------+
| LOGO          VisionQC                  System Status   Menu |
+---------------+----------------------------------------------+
|               |                                              |
| Overview      |  PAGE TITLE                                  |
|               |  Supporting description                      |
| Inspection    |                                              |
|               |  +------------------+ +--------------------+  |
| Experiments   |  |                  | |                    |  |
|               |  |  MAIN CONTENT    | |  SUPPORTING PANEL  |  |
| Datasets      |  |                  | |                    |  |
|               |  +------------------+ +--------------------+  |
| Pipelines     |                                              |
|               |  +----------------------------------------+  |
| Model Registry|  |                                        |  |
|               |  |  TABLE / CHART / DATA VISUALIZATION    |  |
| Monitoring    |  |                                        |  |
|               |  +----------------------------------------+  |
| Retraining    |                                              |
|               |                                              |
| Documentation |                                              |
+---------------+----------------------------------------------+
```

## 5.2 Sidebar

The sidebar should be visually quiet and functional.

Recommended width:

- Expanded: 240px.
- Collapsed: 72px.

Navigation order:

1. Overview
2. Inspection
3. Experiments
4. Datasets
5. Pipelines
6. Model Registry
7. Monitoring
8. Retraining
9. Documentation

Use Lucide icons with consistent stroke weight.

Do not use emoji icons.

The active navigation item should use a subtle blue-tinted background and a clear active indicator.

## 5.3 Top navigation

The top bar should contain:

- Product identity.
- Current page context or breadcrumb.
- Current model version where relevant.
- System health indicator.
- Relevant page actions.

Avoid unnecessary profile avatars or decorative controls.

There is no authentication requirement in the current PRD, so do not add a login, signup or account-management interface.

## 5.4 Content width

Recommended:

- Maximum content width: 1440px.
- Main page padding: 32px.
- Section spacing: 32-40px.
- Card internal padding: 20-24px.
- Mobile page padding: 16px.

Use a consistent spacing scale based on 4px increments.

---

# 6. Component Design System

## 6.1 Buttons

Buttons should be rectangular with modest corner rounding.

Recommended border radius:

- Primary buttons: 5px.
- Secondary buttons: 5px.
- Inputs: 5px.
- Cards: 6px.
- Dialogs: 8px.

No pill-shaped buttons.

### Primary button

- Steel Blue background.
- White text.
- Medium font weight.
- Clear hover state.
- Visible keyboard focus.

### Secondary button

- White or transparent background.
- Grey border.
- Dark text.

### Destructive button

- Restrained red treatment.
- Used only for destructive actions.

### Button dimensions

- Height: 38-42px.
- Horizontal padding: 14-18px.
- Font size: 13-14px.

Avoid oversized buttons.

## 6.2 Cards

Cards should have:

- White background.
- Thin border.
- Minimal or no shadow.
- Consistent internal spacing.
- Clear heading and content hierarchy.

Avoid:

- Excessive rounded corners.
- Large floating shadows.
- Gradient backgrounds.
- Decorative icons inside every card.
- Cards containing fabricated metrics.

Cards should group related information, not simply fill empty space.

## 6.3 Tables

Tables are important because VisionQC is a data-driven application.

Use tables for:

- Experiment history.
- Dataset versions.
- Model registry.
- Pipeline executions.
- Prediction history.
- Retraining records.

Table design:

- Clear column headers.
- Thin row separators.
- Consistent row height.
- Right alignment for numerical values where appropriate.
- Monospace for IDs and version references.
- Clear empty and loading states.
- Functional sorting and filtering where implemented.

Avoid excessive borders around every individual cell.

## 6.4 Status indicators

Use compact status labels.

Examples:

- OK
- DEFECTIVE
- RUNNING
- FAILED
- COMPLETED
- PENDING
- DRIFT DETECTED

Use a subtle background tint and readable text.

Status indicators should not become oversized decorative badges.

## 6.5 Inputs

Inputs should use:

- White background.
- Thin grey border.
- 5px corner radius.
- Clear labels.
- Consistent height.
- Visible focus state.
- Descriptive validation messages.

Never rely on placeholder text as the only label.

## 6.6 Dialogs and drawers

Use dialogs for:

- Confirming destructive actions.
- Viewing detailed prediction information.
- Reviewing model metadata.
- Confirming retraining actions.

Use drawers for contextual details when keeping the underlying page visible improves navigation.

Keep dialog sizes proportional to their content.

---

# 7. Page-by-Page Design Direction

## 7.1 Overview Dashboard

**Purpose:** Show the current operational state of VisionQC.

The overview should answer:

- Is the inspection API working?
- Which model is currently deployed?
- Are recent inspections succeeding?
- Is there an active pipeline?
- Has drift been detected?
- Does any issue require attention?

### Layout

Top section:

- Page title: `Overview`
- Supporting copy: `Current inspection and model operations.`
- Last updated timestamp.

Main section:

- API health.
- Active model version.
- Recent inspection count.
- Latest pipeline state.

Secondary section:

- Prediction distribution.
- Recent pipeline activity.
- Recent model evaluation.
- Monitoring alerts.

### Important

All values must come from actual system data.

If no predictions exist, show an empty state.

Do not display fabricated values such as:

- 98.9% accuracy.
- 10,000 inspections completed.
- 99.99% uptime.
- 500+ happy customers.

A missing value is better than a fabricated value.

## 7.2 Inspection Page

**Purpose:** Allow users to upload an impeller image and inspect the model result.

This is the most important page in VisionQC.

### Layout

```text
+------------------------------------------------------+
| INSPECTION                                           |
| Analyze a pump impeller image                        |
+------------------------------------------------------+
|                                                      |
| +------------------------+ +-----------------------+ |
| |                        | |                       | |
| |   IMAGE UPLOAD         | |   INSPECTION RESULT   | |
| |                        | |                       | |
| |   Image preview        | |   OK / DEFECTIVE      | |
| |                        | |   Confidence          | |
| |                        | |   Model version       | |
| +------------------------+ +-----------------------+ |
|                                                      |
| +--------------------------------------------------+ |
| | GRAD-CAM                                          | |
| | Original image / Heatmap / Overlay               | |
| +--------------------------------------------------+ |
+------------------------------------------------------+
```

### Required components

- Image upload.
- Image preview.
- File validation.
- Analyze button.
- Loading state.
- Prediction result.
- Confidence score.
- Model version.
- Inference latency.
- Grad-CAM visualization.

### Result design

Use clear classification states.

**OK**

- Green status.
- Explicit `OK` label.
- Confidence value.

**DEFECTIVE**

- Red status.
- Explicit `DEFECTIVE` label.
- Confidence value.

Do not use colour as the only indicator.

### Grad-CAM

Provide three viewing modes:

1. Original image.
2. Heatmap.
3. Overlay.

Use actual generated Grad-CAM output.

Do not create decorative heatmaps or synthetic defect markings.

## 7.3 Experiments Page

**Purpose:** Compare model training runs.

### Layout

- Experiment list.
- Model architecture.
- Dataset version.
- Training configuration.
- Metrics.
- Run status.
- Training duration.

### Model comparison

Show actual results for:

- Custom CNN.
- ResNet18.
- EfficientNet-B0.

Recommended metrics:

- Accuracy.
- Precision.
- Defect recall.
- F1-score.
- ROC-AUC.
- PR-AUC.
- False-negative rate.

Defect recall should receive particular emphasis because missed defects are important in manufacturing inspection.

Use charts only when they help compare actual experiment results.

## 7.4 Datasets Page

**Purpose:** Manage and inspect dataset versions.

Display:

- Dataset name.
- Version.
- Number of images.
- OK image count.
- DEFECTIVE image count.
- Split information.
- Augmentation status.
- DVC reference.

Use compact tables and metadata panels.

Do not create fake dataset version histories.

## 7.5 Pipelines Page

**Purpose:** Monitor Airflow workflows.

Display:

- DAG name.
- Latest execution.
- Run status.
- Start time.
- Duration.
- Failed task count.
- Next scheduled run, if applicable.

Provide a detailed execution view showing task dependencies and statuses.

Use a structured workflow visualization rather than an ornamental animated flowchart.

## 7.6 Model Registry Page

**Purpose:** Track model versions and deployment state.

Display:

- Model name.
- Model architecture.
- Version.
- Dataset reference.
- Evaluation metrics.
- Registration date.
- Approval state.
- Deployment state.

Make the active deployed model visually clear.

Model promotion should be an explicit, controlled operation.

## 7.7 Monitoring Page

**Purpose:** Observe application and ML behavior.

Separate the page into two sections.

### Operational monitoring

- API request volume.
- Error rate.
- Latency.
- Throughput.
- Service health.

### ML monitoring

- Prediction distribution.
- Confidence distribution.
- Image drift.
- Reference versus incoming feature distributions.
- Model performance when actual labels are available.

Use restrained charts with clear axis labels, units and time ranges.

## 7.8 Retraining Page

**Purpose:** Monitor and control retraining workflows.

Display:

- Drift status.
- Trigger reason.
- Dataset version.
- Retraining run.
- Evaluation result.
- Quality-gate status.
- Promotion decision.

A drift alert must not automatically replace the deployed model.

Show the difference between:

- Retraining requested.
- Training running.
- Evaluation completed.
- Quality gate passed.
- Model approved.
- Model deployed.

## 7.9 Documentation Page

**Purpose:** Provide project and model documentation.

Include:

- Architecture.
- Dataset documentation.
- Model card.
- Training methodology.
- Evaluation methodology.
- API documentation.
- Known limitations.

Use a readable documentation layout with clear headings and tables.

---

# 8. Signature Visual Element

## The Inspection Workbench

VisionQC should have one recognizable visual feature: the Inspection Workbench.

This is a dedicated workspace that brings together:

- Original impeller image.
- Model prediction.
- Confidence score.
- Grad-CAM visualization.
- Model version.
- Inference time.

The workbench should be designed like a technical inspection instrument rather than a generic image-upload card.

### Visual treatment

- Neutral background.
- Strong image presentation.
- Thin structural borders.
- Dark technical information panel.
- Restrained status colours.
- Clear image comparison controls.

This should become the defining visual component of VisionQC.

It communicates what the application actually does.

---

# 9. Charts and Data Visualization

Charts must be functional and accurate.

## Recommended chart styles

| Chart | Usage |
|---|---|
| Bar chart | Model comparison |
| Line chart | Latency and request trends |
| Donut chart | Prediction distribution |
| Histogram | Confidence distribution |
| Confusion matrix | Classification evaluation |
| Heatmap | Grad-CAM visualization |
| Timeline | Pipeline and retraining history |

### Chart rules

1. Use real data.
2. Label axes.
3. Show units.
4. Provide meaningful tooltips.
5. Avoid unnecessary chart legends.
6. Avoid 3D charts.
7. Do not use gradients as chart fills.
8. Do not use excessive colours.
9. Display empty states when no data exists.
10. Distinguish missing data from zero.

Use consistent colours across all charts.

---

# 10. Motion and Interaction

Motion should be restrained and purposeful.

## 10.1 Allowed animations

| Interaction | Animation |
|---|---|
| Page transition | Subtle opacity transition |
| Modal opening | Short opacity and scale transition |
| Sidebar collapse | Width transition |
| Button hover | Background or border transition |
| Tab selection | Short indicator transition |
| Chart loading | Minimal loading state |
| Image comparison | Direct interaction without excessive animation |
| Status change | Subtle visual state transition |

## 10.2 Timing

Recommended durations:

- Hover: 120-160ms.
- Button transitions: 120-180ms.
- Modal transitions: 160-220ms.
- Sidebar transitions: 180-240ms.

Use simple easing.

## 10.3 Strictly prohibited

- Cursor-following animations.
- Custom animated cursors.
- Excessive scroll-triggered reveals.
- Parallax backgrounds.
- Continuous floating elements.
- Animated gradients.
- Random bouncing icons.
- Unnecessary number-counting animations.
- Long page entrance sequences.
- Motion that delays access to important information.

Respect `prefers-reduced-motion`.

---

# 11. Copywriting and Content Standards

The writing style must be direct, specific and technically accurate.

## 11.1 Preferred language

Use:

- Inspect image.
- Run prediction.
- View model details.
- Compare experiments.
- Open pipeline.
- View drift report.
- Start retraining.
- Review evaluation.
- View model version.

Avoid:

- Unlock the power of AI.
- Revolutionizing manufacturing.
- Next-generation intelligence.
- Experience the future.
- Transforming quality forever.
- Unleash intelligent automation.

## 11.2 Hero copy

If VisionQC has a public landing page, the hero should explain exactly what the project does.

Suggested direction:

**Headline:**

Automated defect inspection for pump impellers.

**Supporting text:**

Analyze impeller images, review classification results and track model performance through a reproducible MLOps workflow.

**Primary action:**

Open inspection dashboard.

**Secondary action:**

View system architecture.

No vague slogans or exaggerated claims.

## 11.3 Empty states

Empty states should explain what is missing and what the user can do.

Examples:

**No inspections yet**

Upload an impeller image to run your first inspection.

**No experiments available**

Run the training pipeline to create an experiment record.

**No drift reports available**

Drift measurements will appear after incoming image data has been evaluated.

**No pipeline executions**

No Airflow runs have been recorded yet.

---

# 12. Responsive Design

The application must work across desktop, tablet and mobile.

## Desktop

- Full sidebar.
- Multi-column layouts.
- Larger image comparison areas.
- Full data tables.

## Tablet

- Collapsible sidebar.
- Reduced column count.
- Responsive charts.
- Scrollable tables when required.

## Mobile

- Compact navigation.
- Single-column layout.
- Full-width inspection image.
- Stacked prediction details.
- Touch-friendly controls.
- No horizontal page overflow.

The inspection workflow must remain usable on mobile.

---

# 13. Accessibility

Target WCAG 2.2 AA.

Requirements:

- Sufficient text contrast.
- Visible keyboard focus.
- Semantic HTML.
- Proper form labels.
- Accessible status messages.
- Keyboard-accessible dialogs.
- Descriptive image alternatives.
- Reduced-motion support.
- Clear validation messages.
- No colour-only status communication.

Do not sacrifice accessibility for visual styling.

---

# 14. Technical Implementation

The design system should use the approved VisionQC stack.

| Area | Technology |
|---|---|
| Framework | Next.js |
| UI library | React |
| Language | TypeScript |
| Styling | Tailwind CSS |
| Components | shadcn/ui + Radix UI |
| Icons | Lucide React |
| Charts | Recharts |
| Motion | Framer Motion |

## 14.1 Suggested design tokens

Create a centralized token system.

Example:

```css
:root {
  /* Primary surfaces */
  --color-ink: #111820;
  --color-graphite: #202A35;
  --color-paper: #F5F6F5;
  --color-white: #FFFFFF;

  /* Brand */
  --color-steel-blue: #476985;
  --color-muted-blue: #7892A8;

  /* Supporting */
  --color-border: #DCE1E4;
  --color-muted-grey: #687580;
  --color-light-grey: #EBEEF0;

  /* Semantic */
  --color-success: #34765B;
  --color-danger: #B64B46;
  --color-warning: #B27A32;
  --color-info: #476985;

  /* Typography */
  --font-display: "Roobert", "Geist Sans", sans-serif;
  --font-body: "Roobert", "Geist Sans", sans-serif;
  --font-mono: "Geist Mono", monospace;

  /* Radius */
  --radius-button: 5px;
  --radius-input: 5px;
  --radius-card: 6px;
  --radius-dialog: 8px;

  /* Borders */
  --border-default: 1px solid var(--color-border);
}
```

All shared components should consume these tokens.

Do not introduce arbitrary colours or radius values in individual pages.

## 14.2 Component organization

Suggested frontend structure:

```text
frontend/
├── app/
│   ├── overview/
│   ├── inspection/
│   ├── experiments/
│   ├── datasets/
│   ├── pipelines/
│   ├── model-registry/
│   ├── monitoring/
│   ├── retraining/
│   └── documentation/
│
├── components/
│   ├── layout/
│   ├── navigation/
│   ├── buttons/
│   ├── tables/
│   ├── charts/
│   ├── inspection/
│   ├── model/
│   ├── monitoring/
│   └── shared/
│
├── hooks/
├── lib/
├── services/
├── types/
└── styles/
```

Avoid duplicating the same component styles across pages.

---

# 15. Design Quality Rules

These rules are mandatory.

## 15.1 Never use

- Purple gradients.
- Pill-shaped buttons.
- Fake reviews.
- Fake metrics.
- Fake customer counters.
- Vague hero copy.
- Emoji icons.
- Em dashes in website copy.
- AI-generated stock-looking photos.
- Generic AI-generated marketing illustrations.
- Cursor animations.
- Over-the-top scroll animations.
- Decorative animated backgrounds.
- Fake activity feeds.
- Fake testimonials.
- Fake company logos.
- Fabricated performance claims.
- Unnecessary glassmorphism.
- Excessive shadows.
- Random decorative elements.

## 15.2 Content authenticity

Use:

- Real inspection images from the dataset.
- Actual prediction results.
- Real model evaluation metrics.
- Actual pipeline execution records.
- Real experiment information.
- Genuine system health data.
- Actual Grad-CAM visualizations.

When data is unavailable, show a clear empty state.

Never fill empty dashboard space with invented information.

## 15.3 Design consistency

Every page must use:

- The same typography system.
- The same colour tokens.
- The same button styles.
- The same border treatment.
- The same spacing scale.
- The same icon system.
- The same interaction patterns.

A new page must not introduce a separate visual identity.

---

# 16. Launch Requirements

VisionQC must not be considered ready for public launch until every required item below is complete.

## 16.1 Branding

- [ ] Custom domain connected.
- [ ] Favicon added.
- [ ] Correct product name and branding.
- [ ] No placeholder logos.
- [ ] No broken images or assets.

## 16.2 Platform

- [ ] Remove all "Made with AI" labels or badges.
- [ ] Verify responsive layouts.
- [ ] Verify all navigation links.
- [ ] Verify all primary actions.
- [ ] Verify API integration.
- [ ] Verify error and empty states.
- [ ] Verify no fabricated metrics.
- [ ] Verify no broken routes.

## 16.3 Legal

- [ ] Privacy Policy page published.
- [ ] Terms and Conditions page published.
- [ ] Legal pages linked from the footer.
- [ ] Legal content reviewed for the actual data collection and usage.

Do not copy generic legal templates without reviewing them against the actual product.

## 16.4 Quality assurance

- [ ] Test desktop layout.
- [ ] Test tablet layout.
- [ ] Test mobile layout.
- [ ] Test keyboard navigation.
- [ ] Test visible focus states.
- [ ] Test reduced-motion settings.
- [ ] Test loading states.
- [ ] Test failed API requests.
- [ ] Test empty data states.
- [ ] Test actual inspection workflow.
- [ ] Test model information accuracy.
- [ ] Test all dashboard metrics against their sources.

**Launch rule:** If any mandatory launch item is incomplete, the public launch is blocked.

---

# 17. Implementation Priority

The design should be implemented in this order.

| Priority | Task |
|---|---|
| P0 | Establish design tokens and typography |
| P0 | Build application shell and navigation |
| P0 | Build Inspection Workbench |
| P0 | Build prediction result components |
| P1 | Build Overview dashboard |
| P1 | Build Experiments and Model Registry |
| P1 | Build Datasets and Pipelines |
| P1 | Build Monitoring and Retraining |
| P2 | Add refined transitions and interactions |
| P2 | Responsive polish |
| P2 | Accessibility review |
| P3 | Custom domain, favicon and launch preparation |
| P3 | Privacy Policy and Terms pages |

Build the shared design foundation before implementing every individual page.

---

# 18. Final Design Direction

VisionQC should feel like a real industrial inspection product.

Its visual identity should come from the quality of its layout, typography, image presentation and data visualization.

The reference website provides inspiration for its confidence, hierarchy and restraint. VisionQC should apply those qualities to a manufacturing and MLOps context.

**The defining experience is the Inspection Workbench.**

A user should be able to open an impeller image, inspect the prediction, understand the model's confidence and review the Grad-CAM visualization without unnecessary visual distractions.

The interface should be confident, precise, functional and honest.

**Design principle: Show the system working. Never decorate it to look like it is working.**