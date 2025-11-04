# Puerto Usage Examples

**Real-world project workflows using the digital agency team**

---

## Table of Contents

1. [Building a SaaS Product (End-to-End)](#example-1-building-a-saas-product)
2. [Launching a Marketing Campaign](#example-2-launching-a-marketing-campaign)
3. [Bug Fix and Hotfix Deployment](#example-3-bug-fix-and-hotfix-deployment)
4. [Design System Creation](#example-4-design-system-creation)
5. [Data Analytics Dashboard](#example-5-data-analytics-dashboard)
6. [Mobile App Launch](#example-6-mobile-app-launch)

---

## Example 1: Building a SaaS Product

**Scenario:** Build a project management SaaS from scratch

### Phase 1: Discovery (Week 1-2)

**Step 1: Define Vision and Strategy**
```
User: "I want to build a project management tool for remote teams.
       Help me define the product vision and strategy."

→ Invoke: leadership/chief-strategy-officer
```

**What the CSO does:**
- Conducts competitive analysis
- Defines unique value proposition
- Creates strategic positioning
- Identifies target market segments

**Deliverable:** Product vision document, strategic positioning

---

**Step 2: User Research**
```
User: "What do remote teams need most in project management tools?"

→ Invoke: design/ux-researcher
```

**What the UX Researcher does:**
- Creates research plan
- Designs interview guides
- Conducts user interviews
- Synthesizes insights

**Deliverable:** User research report with pain points and needs

---

**Step 3: Requirements Gathering**
```
User: "Based on the research, what features should we build?"

→ Invoke: product/business-analyst
```

**What the Business Analyst does:**
- Translates user needs into requirements
- Creates user stories
- Prioritizes features (MoSCoW)
- Estimates effort and resources

**Deliverable:** Requirements specification with prioritized backlog

---

### Phase 2: Design (Week 3-5)

**Step 4: Information Architecture**
```
User: "Design the information architecture for the PM tool."

→ Invoke: design/design-lead
```

**What the Design Lead does:**
- Creates sitemap
- Designs navigation structure
- Defines user flows
- Plans component hierarchy

**Deliverable:** IA documentation and user flow diagrams

---

**Step 5: Wireframes and Prototypes**
```
User: "Create wireframes for the dashboard and project views."

→ Invoke: design/ux-researcher
```

**What the UX Researcher does:**
- Creates low-fidelity wireframes
- Builds interactive prototype
- Conducts usability testing
- Iterates based on feedback

**Deliverable:** Wireframes and tested prototype

---

**Step 6: Content Strategy**
```
User: "What should our microcopy and messaging be?"

→ Invoke: design/ux-writer
```

**What the UX Writer does:**
- Defines voice and tone
- Writes microcopy for UI
- Creates error messages
- Develops onboarding copy

**Deliverable:** Content style guide and microcopy library

---

### Phase 3: Development (Week 6-12)

**Step 7: Technical Architecture**
```
User: "Design the technical architecture for scalability."

→ Invoke: engineering/engineering-lead
```

**What the Engineering Lead does:**
- Designs system architecture
- Chooses tech stack
- Plans database schema
- Defines API contracts

**Deliverable:** Architecture documentation and tech stack decisions

---

**Step 8: Backend Development**
```
User: "Build the REST API with authentication and project management endpoints."

→ Invoke: engineering/backend-engineer
```

**What the Backend Engineer does:**
- Implements authentication (JWT)
- Builds project CRUD APIs
- Creates task management endpoints
- Implements real-time updates (WebSockets)

**Deliverable:** Backend API with documentation

---

**Step 9: Frontend Development**
```
User: "Build the React frontend with dashboard, project views, and task boards."

→ Invoke: engineering/frontend-engineer
```

**What the Frontend Engineer does:**
- Sets up React + TypeScript project
- Implements design system components
- Builds dashboard and views
- Integrates with backend API

**Deliverable:** Frontend application

---

**Step 10: Testing**
```
User: "Create comprehensive test coverage for the application."

→ Invoke: engineering/qa-engineer
```

**What the QA Engineer does:**
- Writes unit tests (Jest)
- Creates integration tests
- Builds E2E test suite (Playwright)
- Performs exploratory testing

**Deliverable:** Test suite with 80%+ coverage

---

### Phase 4: Deployment (Week 13)

**Step 11: Infrastructure Setup**
```
User: "Set up production infrastructure on AWS with CI/CD."

→ Invoke: engineering/devops-engineer
```

**What the DevOps Engineer does:**
- Creates Terraform IaC
- Sets up Kubernetes cluster
- Configures CI/CD pipeline (GitHub Actions)
- Implements monitoring (DataDog)

**Deliverable:** Production infrastructure and deployment pipeline

---

**Step 12: Launch Planning**
```
User: "Create the go-to-market launch plan."

→ Invoke: marketing/marketing-director
```

**What the Marketing Director does:**
- Defines launch strategy
- Creates launch timeline
- Plans marketing channels
- Coordinates launch activities

**Deliverable:** Launch plan and timeline

---

### Phase 5: Growth (Week 14+)

**Step 13: Content Marketing**
```
User: "Create a content marketing strategy to drive signups."

→ Invoke: marketing/content-strategist
```

**What the Content Strategist does:**
- Creates content calendar
- Writes blog posts on project management
- Develops lead magnets
- Plans email nurture campaigns

**Deliverable:** Content calendar and published content

---

**Step 14: Analytics Setup**
```
User: "Set up analytics to track user behavior and conversion."

→ Invoke: product/data-analyst
```

**What the Data Analyst does:**
- Implements analytics (Mixpanel)
- Creates dashboards
- Defines key metrics
- Sets up conversion funnels

**Deliverable:** Analytics dashboards and KPI tracking

---

**Step 15: Growth Experiments**
```
User: "Run growth experiments to improve conversion."

→ Invoke: marketing/growth-marketer
```

**What the Growth Marketer does:**
- Designs A/B tests
- Optimizes onboarding flow
- Tests pricing page variations
- Analyzes experiment results

**Deliverable:** Growth experiment results and recommendations

---

## Example 2: Launching a Marketing Campaign

**Scenario:** Launch a product announcement campaign across channels

### Step 1: Campaign Strategy
```
User: "Plan a product launch campaign for our new feature."

→ Invoke: marketing/marketing-director
```

**Deliverables:**
- Campaign objectives and KPIs
- Channel strategy (blog, email, social, PR)
- Timeline and budget
- Success metrics

---

### Step 2: Content Creation
```
User: "Write the launch announcement blog post and email campaign."

→ Invoke: marketing/content-strategist
```

**Deliverables:**
- Launch blog post
- Email sequence (teaser, launch, follow-up)
- Press release
- FAQ content

---

### Step 3: SEO Optimization
```
User: "Optimize the launch content for search engines."

→ Invoke: marketing/seo-specialist
```

**Deliverables:**
- Keyword research
- On-page SEO optimization
- Meta descriptions
- Internal linking strategy

---

### Step 4: Social Media Campaign
```
User: "Create social media campaign to promote the launch."

→ Invoke: marketing/social-media-manager
```

**Deliverables:**
- Social media calendar
- Post copy and hashtags
- Visual content plan
- Engagement strategy

---

### Step 5: Performance Tracking
```
User: "Track campaign performance and report on results."

→ Invoke: product/data-analyst
```

**Deliverables:**
- Campaign dashboard
- Traffic and conversion metrics
- ROI analysis
- Optimization recommendations

---

## Example 3: Bug Fix and Hotfix Deployment

**Scenario:** Critical bug discovered in production

### Step 1: Bug Diagnosis
```
User: "Users are reporting payment failures. Debug the issue."

→ Invoke: engineering/backend-engineer
```

**What the Backend Engineer does:**
- Reviews error logs
- Reproduces the issue
- Identifies root cause (Stripe API timeout)
- Proposes fix

---

### Step 2: Fix Implementation
```
User: "Implement the fix with proper error handling and retries."

→ Invoke: engineering/backend-engineer
```

**What the Backend Engineer does:**
- Adds retry logic with exponential backoff
- Implements circuit breaker
- Adds comprehensive logging
- Tests fix locally

---

### Step 3: Testing
```
User: "Verify the fix works and doesn't introduce regressions."

→ Invoke: engineering/qa-engineer
```

**What the QA Engineer does:**
- Tests payment flow end-to-end
- Verifies error scenarios
- Runs regression test suite
- Approves for deployment

---

### Step 4: Hotfix Deployment
```
User: "Deploy the hotfix to production with zero downtime."

→ Invoke: engineering/devops-engineer
```

**What the DevOps Engineer does:**
- Creates hotfix branch
- Deploys to staging
- Performs blue-green deployment
- Monitors production metrics

---

### Step 5: Customer Communication
```
User: "Notify affected customers about the fix."

→ Invoke: sales/customer-success-manager
```

**What the Customer Success Manager does:**
- Identifies affected customers
- Drafts status update email
- Sends personalized follow-ups
- Monitors support tickets

---

## Example 4: Design System Creation

**Scenario:** Build a comprehensive design system from scratch

### Step 1: Design System Strategy
```
User: "Plan our design system including components, tokens, and documentation."

→ Invoke: design/design-lead
```

**Deliverables:**
- Design system roadmap
- Component inventory
- Design token taxonomy
- Governance model

---

### Step 2: Accessibility Audit
```
User: "Ensure our design system meets WCAG 2.1 Level AA compliance."

→ Invoke: design/accessibility-specialist
```

**Deliverables:**
- Accessibility audit report
- Color contrast recommendations
- Keyboard navigation patterns
- ARIA attribute guidelines

---

### Step 3: Component Design
```
User: "Design the core component library (buttons, forms, cards, etc.)."

→ Invoke: design/design-lead
```

**Deliverables:**
- Figma component library
- Design tokens (colors, typography, spacing)
- Component specifications
- Usage guidelines

---

### Step 4: Component Documentation
```
User: "Write clear documentation for each component with usage examples."

→ Invoke: design/ux-writer
```

**Deliverables:**
- Component documentation
- Usage guidelines
- Do's and don'ts
- Code examples

---

### Step 5: Component Implementation
```
User: "Build the React component library with TypeScript and Storybook."

→ Invoke: engineering/frontend-engineer
```

**Deliverables:**
- React component library
- Storybook documentation
- NPM package
- TypeScript types

---

## Example 5: Data Analytics Dashboard

**Scenario:** Build a business intelligence dashboard

### Step 1: Requirements Gathering
```
User: "What metrics and KPIs should our executive dashboard show?"

→ Invoke: product/business-analyst
```

**Deliverables:**
- Stakeholder interviews
- KPI framework
- Dashboard requirements
- Data source inventory

---

### Step 2: Data Pipeline
```
User: "Build ETL pipeline to aggregate data from multiple sources."

→ Invoke: engineering/data-engineer
```

**Deliverables:**
- ETL pipeline (Airflow)
- Data warehouse schema (Snowflake)
- Data quality checks
- Automated data refresh

---

### Step 3: Dashboard Design
```
User: "Design the dashboard layout and visualizations."

→ Invoke: product/data-analyst
```

**Deliverables:**
- Dashboard wireframes
- Visualization specifications
- Metric definitions
- Interactive filters design

---

### Step 4: Dashboard Implementation
```
User: "Build the interactive dashboard with real-time data."

→ Invoke: engineering/frontend-engineer
```

**Deliverables:**
- Dashboard web app (React + D3.js)
- Real-time data updates (WebSockets)
- Export functionality (PDF, CSV)
- Mobile-responsive design

---

### Step 5: Analytics Insights
```
User: "Analyze the data and provide actionable insights."

→ Invoke: product/data-analyst
```

**Deliverables:**
- Weekly insights report
- Trend analysis
- Anomaly detection
- Recommendations

---

## Example 6: Mobile App Launch

**Scenario:** Launch iOS and Android apps

### Step 1: Mobile Strategy
```
User: "Should we build native or cross-platform? Plan our mobile strategy."

→ Invoke: engineering/engineering-lead
```

**Deliverables:**
- Native vs cross-platform analysis
- Technology recommendation (React Native)
- Architecture plan
- Resource requirements

---

### Step 2: Mobile Development
```
User: "Build the React Native app for iOS and Android."

→ Invoke: engineering/mobile-engineer
```

**Deliverables:**
- React Native application
- Platform-specific code (iOS/Android)
- Push notification integration
- Offline mode support

---

### Step 3: Mobile Testing
```
User: "Test the app on multiple devices and OS versions."

→ Invoke: engineering/qa-engineer
```

**Deliverables:**
- Device compatibility testing
- Performance testing
- Battery and memory profiling
- App store compliance check

---

### Step 4: App Store Optimization
```
User: "Optimize our app store listings for discoverability."

→ Invoke: marketing/seo-specialist
```

**Deliverables:**
- Keyword research (App Store, Play Store)
- App title and description optimization
- Screenshot and video guidelines
- Review generation strategy

---

### Step 5: Mobile Launch Campaign
```
User: "Create a launch campaign to drive app downloads."

→ Invoke: marketing/marketing-director
```

**Deliverables:**
- Launch campaign plan
- App install ads (iOS/Android)
- Influencer partnerships
- Press outreach

---

## Sequential Workflow Patterns

### Research → Design → Build Pattern

```
1. design/ux-researcher (User research)
2. design/design-lead (Design direction)
3. design/ux-writer (Content strategy)
4. engineering/frontend-engineer (Implementation)
5. engineering/qa-engineer (Testing)
```

---

### Strategy → Plan → Execute Pattern

```
1. leadership/chief-strategy-officer (Vision & strategy)
2. product/chief-product-officer (Product roadmap)
3. product/project-manager (Project plan)
4. engineering/engineering-lead (Technical plan)
5. [Engineering team] (Execution)
```

---

### Build → Test → Deploy → Monitor Pattern

```
1. engineering/[any-engineer] (Implementation)
2. engineering/qa-engineer (Testing)
3. engineering/devops-engineer (Deployment)
4. engineering/devops-engineer (Monitoring)
5. sales/customer-success-manager (User support)
```

---

### Content → SEO → Social → Analytics Pattern

```
1. marketing/content-strategist (Content creation)
2. marketing/seo-specialist (SEO optimization)
3. marketing/social-media-manager (Social promotion)
4. marketing/growth-marketer (Optimization)
5. product/data-analyst (Performance tracking)
```

---

## Tips for Success

### 1. Always Start with Strategy
Before diving into tactics, invoke the Chief Strategy Officer or relevant department lead to set direction.

### 2. Follow Sequential Workflows
Don't skip phases. Discovery → Design → Build → Deploy → Grow is the proven path.

### 3. Involve QA Early
Bring in the QA Engineer during development, not just at the end.

### 4. Cross-Department Collaboration
Most projects need multiple departments. Plan for collaboration from the start.

### 5. Track and Measure
Always involve the Data Analyst to set up tracking and measure success.

### 6. Iterate Based on Data
Use the Growth Marketer to run experiments and optimize continuously.

---

## Common Mistakes to Avoid

❌ **Skipping Research** - Building without user validation
✅ **Do Research First** - Always start with design/ux-researcher

❌ **No Testing** - Deploying untested code
✅ **Test Thoroughly** - Always involve engineering/qa-engineer

❌ **Launching Without Analytics** - Not tracking success
✅ **Set Up Tracking** - Always involve product/data-analyst

❌ **Building in Isolation** - Single department working alone
✅ **Collaborate Cross-Functionally** - Involve multiple departments

❌ **No Launch Plan** - Building with no go-to-market
✅ **Plan the Launch** - Always involve marketing/marketing-director

---

**Version:** 1.0.0
**Last Updated:** 2025-11-03
**Examples:** 6 end-to-end workflows with 50+ role invocations
